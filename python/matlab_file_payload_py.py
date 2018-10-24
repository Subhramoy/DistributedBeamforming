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

    bmwght_temp = []
    bmfrm_pyld = []
    beamform_payload = []
    beamweights = []

    counter = 0

    def __init__(self, file_path):
        gr.basic_block.__init__(self,
                                name="matlab_file_payload_py",
                                in_sig=None,
                                out_sig=[numpy.complex64])

        file_path = "/home/gokhan/gnu-radio/gr-beamforming/examples/data/"

        # Real part of the payload read from 'payload_real.txt' file
        with open(file_path + 'payload_real.txt', 'r') as f:
            pay_real = [line.strip() for line in f]

        length = (len(pay_real))

        # Imaginary part of the payload read from 'payload_imag.txt' file
        with open(file_path + 'payload_imag.txt', 'r') as f1:
            pay_imag = [line.strip() for line in f1]

        # Reconstructing the payload in complex format
        for ii in range(length):
            data_p_c = complex(float(pay_real[ii]), float(pay_imag[ii]))
            data = numpy.complex64(data_p_c)
            self.payload.append(data)

    def forecast(self, noutput_items, ninput_items_required):
        print("This function should not be called")
        # setup size of input_items[i] for work call
        for i in range(len(ninput_items_required)):
            ninput_items_required[i] = noutput_items

    def general_work(self, input_items, output_items):

        # print("Function CALLED without any input\n")

        if (self.counter == len(self.payload)):
            self.counter = 0

        data_send = self.payload[self.counter]
        self.counter = self.counter + 1

        output_items[0][:] = data_send
        return len(output_items[0])
