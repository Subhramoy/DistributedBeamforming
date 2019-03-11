#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2019 Genesys Lab..
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

import os
import numpy
import logging
import pmt
from gnuradio import gr

class feedback_calculation_py(gr.basic_block):
    """
    docstring for block feedback_calculation_py
    """
    def __init__(self, seq_len, frame_len, number_of_Tx, data_path):
        gr.basic_block.__init__(self,
            name="feedback_calculation_py",
            in_sig=[numpy.complex64],
            out_sig=None)

        """Set number of active transmitters"""
        self.number_of_Tx = number_of_Tx
        self.gold_seq_length = seq_len
        self.frame_length = frame_len

        """Logger init"""
        ##  @todo gr-logger is not working as expected, update in CMAKE files might be required.
        #
        self.log = gr.logger(str(__name__))
        self.log.set_level("INFO")


        """Get Gold Sequences"""
        self.log.info("Receiver is initiated for {} active transmitters.".format(number_of_Tx))
        self.gold_sequences = numpy.empty((number_of_Tx, self.gold_seq_length),
                                          numpy.complex64)
        #logging.debug(self.gold_sequences)

        tx_index = 0
        while tx_index < number_of_Tx:
            self.gold_sequences[tx_index,:] = numpy.array(self.get_training_signal(data_path, tx_index))
            tx_index = tx_index + 1

        """Set output message port"""
        self.message_port_register_out(pmt.intern("out"))
        ## Send pmt message through output port
        # weight = pmt.from_complex(self.beamweight)
        # self.message_port_pub(pmt.intern("out"), weight)




    def forecast(self, noutput_items, ninput_items_required):
        # self.log.debug("forecast function call")

        #setup size of input_items[i] for work call
        for i in range(len(ninput_items_required)):
            ninput_items_required[i] = noutput_items

    def general_work(self, input_items, output_items):
        # self.log.debug("General work function call. ")

        tags = self.get_tags_in_window(0, 0, len(input_items[0]))


        if len(tags) > 0:
            self.log.debug("Tag is found.")

        for tag in tags:
            print tag.key
            print tag.value
        ## Calculate the CSI and the mis-alignment
        # Send it to next block

        # output_items[0][:] = input_items[0]
        self.log.debug("Size of input buffer: {}".format(len(input_items[0])))
        self.consume(0, len(input_items[0]))

        #self.consume_each(len(input_items[0]))
        # return len(output_items[0])
        return 0 # There is no output flow


    def get_training_signal(self, file_path, number_Tx):
        """ @todo Define 2D array and return all gold sequence
               streams dynamically w.r.t. given number_Tx parameter.
               @note curently only returns TX1 gold sequence """
        gold_sequence = []

        # Enumeration starts with 1 in files
        Tx_index = int(number_Tx) + 1

        dir_path = os.path.dirname(os.path.realpath(__file__))


        # print "Data Path at cor_and_tag block: {}".format(dir_path)


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


        self.log.info("Training Signal {} is successfully retrieved from the target files."
              .format(Tx_index))

        return gold_sequence