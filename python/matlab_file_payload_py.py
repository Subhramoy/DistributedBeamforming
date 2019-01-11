#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2018 GENESYS Lab..
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

import pmt
import numpy
from gnuradio import gr


class matlab_file_payload_py(gr.sync_block):
    """
    docstring for block matlab_file_payload_py
    """
    numTxAntennas = 1
    binary_byte_read = 8
    channel_est_antennas = []
    payload = []

    counter = 0

    file_path = ""

    def __init__(self, file_path):
        gr.sync_block.__init__(self,
                                name="matlab_file_payload_py",
                                in_sig=[numpy.complex64],
                                out_sig=[numpy.complex64])
        self.file_path = file_path

        # Input and output message ports
        self.message_port_register_in(pmt.intern("generate"))
        self.message_port_register_out(pmt.intern("training_signal"))
        self.set_msg_handler(pmt.intern("generate"), self.send_trainingSignal)


        # Real part of the payload read from 'payload_real.txt' file
        with open( self.file_path + '_real.txt', 'r') as f:
            pay_real = [line.strip() for line in f]

        length = (len(pay_real))

        # Imaginary part of the payload read from 'payload_imag.txt' file
        with open(self.file_path + '_imag.txt', 'r') as f1:
            pay_imag = [line.strip() for line in f1]

        # Reconstructing the payload in complex format
        for ii in range(length):
            data_p_c = complex(float(pay_real[ii]), float(pay_imag[ii]))
            data = numpy.complex64(data_p_c)
            self.payload.append(data)

        print("Training Signal is successfully retrieved from the target file.")



    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # print("Function CALLED without any input\n")

        #if (self.counter == len(self.payload)):
        #    print("END_OF_FILE")
        #    self.counter = 0

        # data_send = self.payload[self.counter]
        # self.counter = self.counter + 1

        # print(self.counter)
        # print("This is the data send:")

        req_size = len(out)

        end = self.counter + req_size
        if end > len(self.payload):
            residue_size = len(self.payload) - self.counter
            remaining_req = req_size - residue_size

            out[:] = numpy.append(
                self.payload[self.counter: len(self.payload)],
                self.payload[0: remaining_req]
            )
            self.counter = remaining_req

            return len(output_items[0])

        else:
            out[:] = self.payload[self.counter:end]
            return len(output_items[0])



    def send_trainingSignal(self, msg):
        print("Send PDU.")
        print(len(self.payload))

        vector = pmt.make_c32vector(len(self.payload), complex(-1.0))


        # pmt::pmt_t vec_pmt(pmt::make_blob(&t_vec[0], t_vec.size()));
        # pmt::pmt_t pdu(pmt::cons(pmt::PMT_NIL, vec_pmt));

        #self.message_port_pub(pmt.intern("training_signal"), vector)



