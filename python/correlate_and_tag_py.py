#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2019 Genesys lab..
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import logging
import numpy, os
from gnuradio import gr
#import queue
import Queue as queue
import pmt
## https://wiki.gnuradio.org/index.php/Types_of_Blocks
#
# import gnuradio.extras


class correlate_and_tag_py(gr.sync_block):
    """
    docstring for block correlate_and_tag_py
    """
    def __init__(self, seq_len, frame_len, num_Tx, file_path):
        gr.sync_block.__init__(self,
            name="correlate_and_tag_py",
            in_sig=[numpy.complex64],
            out_sig=[numpy.complex64, numpy.complex64])

        ## https://wiki.gnuradio.org/index.php/Types_of_Blocks
        #
        # self.set_auto_consume(False)

        self.gold_seq_length = seq_len
        self.frame_length = frame_len

        """Get Gold Sequences"""
        self.gold_sequences = self.get_training_signal( file_path, num_Tx)
        self.buffer = queue.Queue(maxsize=200000)

        self.output = queue.Queue(maxsize=200000)
        self.corr_output = queue.Queue(maxsize=200000)
        """Internal States"""
        self.delay = True
        self.transmit = False

        self.correlation_window = []

    def forecast(self, noutput_items, ninput_items_required):
        print "forecast noutput_items: {} \t " \
              "ninput_items_required: {}"\
            .format(noutput_items,
                    len(ninput_items_required))

        #setup size of input_items[i] for work call
        for i in range(len(ninput_items_required)):
            ninput_items_required[i] = 6000

        print "end of forecast " \
              "ninput_items_required: {}" \
            .format(
                    ninput_items_required[0])

    def general_work(self, input_items, output_items):
        in0 = input_items[0][:len(output_items[0])]
        out = output_items[0]
        # output_items[0][:] = input_items[0]
        print "Size of input: {} buffer".format(len(input_items[0]))
        print "Size of input: {} \t output: {} buffers".format(len(in0), len(out))

        out[:] = in0


        print "Call for consume function with parameter {}".format(len(input_items[0]))
        self.consume(0, len(input_items[0]))
        #self.consume_each(len(input_items[0]))
        return len(output_items[0])


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        corr_out = output_items[1]
        # <+signal processing here+>

        ## Reverse engineering - examining input and output buffers
        # print type(in0)
        # print str(in0.shape)
        # print str(in0.dtype)
        # print str(in0.flags)

        print "Size of input: {} \t output: {}-{} buffers".format(len(in0), len(out), len(corr_out))

        for indx, sample in enumerate(input_items[0]):
            self.buffer.put(sample)

        print "Size of internal buffer: {}".format(self.buffer.qsize())

        # print "Size of output buffer: {}".format(len(out))

        """ Buffer has enough samples to run XCOR"""
        if self.buffer.qsize() + len(self.correlation_window) > self.gold_seq_length + self.frame_length:
            output_head = self.nitems_written(0)
            corr_output_head = self.nitems_written(1)

            read_index = 0
            initial_size = len(self.correlation_window)
            while read_index < self.gold_seq_length + self.frame_length - initial_size:
                self.correlation_window.append(self.buffer.get())
                read_index = read_index + 1


            print "Remaining inputs in buffer: {} \n" \
                  "Number of samples in Cor. window: {}\n".format(
                    self.buffer.qsize(),
                    len(self.correlation_window)
            )

            ## Run xcorrelation
            x_cor_result = numpy.correlate(self.correlation_window,
                                           self.gold_sequences,
                                           mode="same")

            logging.debug( "XCOR output type: {} \t size: {}".format(
                type(x_cor_result),
                len(x_cor_result)))


            ## MATLAB CODE
            # peakIntervals1 = find(abs(crossCorr{1})>(0.8*max(abs(crossCorr{1}))));

            tag_index = numpy.argmax(numpy.absolute(x_cor_result))
            peak_indices = self.get_peaks(x_cor_result)


            key = pmt.intern("example_key")
            value = pmt.intern(str(peak_indices[0]))
            # srcid = pmt.intern("sourceID")



            print self.nitems_written(0)
            print self.nitems_written(1)
            self.add_item_tag(0, output_head
                              + self.output.qsize() # Items waiting in output queue
                              + tag_index, key, value)
            self.add_item_tag(1, corr_output_head
                              + self.corr_output.qsize() # Items waiting in output queue
                              + tag_index, key, value)

            # Push one frame
            push_size = peak_indices[0] + self.frame_length - self.gold_seq_length/2

            print "Sample size pushed to output buffers: {}".format(push_size)
            self.push_data(self.correlation_window[:push_size], "output")
            self.push_data(x_cor_result[:push_size], "correlation_output")

            self.correlation_window = self.correlation_window[push_size:]




        ## Forward the input as is
        # @todo delay and tag
        # corr_out[:] = numpy.ndarray(shape=(len(corr_out),),
        #                            dtype=numpy.complex64)[:len(corr_out)]
        if self.output.qsize() > len(out):
            out[:] =  self.pull_data(len(out), "output")

        if self.corr_output.qsize() > len(corr_out):
            corr_out[:] = self.pull_data(len(corr_out), "correlation_output")

        print "out: {}, c_out: {}, in: {}".format(len(out), len(corr_out), len(in0))
        return len(in0)

    def push_data(self, data_array, output_queue_name):
        if output_queue_name == "output":
            for e in data_array:
                self.output.put(e)
        elif output_queue_name == "correlation_output":
            for e in data_array:
                self.corr_output.put(e)
        else:
            raise Exception("Undefined output queue.")

    def pull_data(self, length, output_queue_name):
        data_array = []
        index = 0

        if output_queue_name == "output":

            if self.output.qsize() < length:
                length = self.output.qsize()

            while index < length:
                data_array.append(self.output.get())
                index = index + 1

        elif output_queue_name == "correlation_output":

            if self.corr_output.qsize() < length:
                length = self.corr_output.qsize()

            while index < length:
                data_array.append(self.corr_output.get())
                index = index + 1
        else:
            raise Exception("Undefined output queue.")

        return data_array
        ##numpy.ndarray(shape=(length,),
        #                     buffer=data_array,
        #                     dtype=numpy.complex64)[:length]

    def get_peaks(self, correlation_output):
        expected_distance = 100

        filtered_candidates = []
        max = numpy.absolute(correlation_output).max()

        peak_candidates = numpy.nonzero(numpy.absolute(correlation_output) > max*0.80)[0]
        print("Values bigger than max*0.80 =", numpy.absolute(correlation_output)[numpy.absolute(correlation_output) > max*0.95])
        print("Their indices are ", peak_candidates)

        t_peak = None
        for candidate in  peak_candidates:
            if t_peak is None:
                t_peak = candidate

            elif abs(candidate - t_peak) < expected_distance: # They are in the same cluster
                if correlation_output[candidate] > correlation_output[t_peak]:
                    t_peak = candidate
            else:
                # candidate belongs to a different cluster
                filtered_candidates.append(t_peak)
                # the first element of next cluster
                t_peak = candidate

        # push the head of last cluster
        filtered_candidates.append(t_peak)

        return filtered_candidates

    def get_training_signal(self, file_path, number_Tx):
        """ @todo Define 2D array and return all gold sequence
               streams dynamically w.r.t. given number_Tx parameter.
               @note curently only returns TX1 gold sequence """
        gold_sequence = []
        Tx_index = 1

        dir_path = os.path.dirname(os.path.realpath(__file__))
        print "Data Path at cor_and_tag block: {}".format(dir_path)

        ## @todo define the loop here ...
        # Real part of the payload read from 'payload_real.txt' file
        with open( file_path + str(Tx_index) + '_real.txt', 'r') as f:
            pay_real = [line.strip() for line in f]

        length = (len(pay_real))

        # Imaginary part of the payload read from 'payload_imag.txt' file
        with open(file_path + str(Tx_index) + '_imag.txt', 'r') as f1:
            pay_imag = [line.strip() for line in f1]

        # Reconstructing the payload in complex format
        for ii in range(length):
            data_p_c = complex(float(pay_real[ii]), float(pay_imag[ii]))
            data = numpy.complex64(data_p_c)
            gold_sequence.append(data)

        print("Training Signal {} is successfully retrieved from the target file."
              .format(Tx_index))

        return gold_sequence
