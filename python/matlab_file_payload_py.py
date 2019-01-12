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


class matlab_file_payload_py(gr.basic_block):
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
        gr.basic_block.__init__(self,
                                name="matlab_file_payload_py",
                                in_sig=None,
                                out_sig=[numpy.complex64])
        self.file_path = file_path

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

    def general_work(self, input_items, output_items):
        out = output_items[0]
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
            self.counter = end
            return len(output_items[0])



