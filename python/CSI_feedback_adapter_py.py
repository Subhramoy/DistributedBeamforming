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

import struct
import pmt
import numpy
import sys
from gnuradio import gr

class CSI_feedback_adapter_py(gr.basic_block):
    """
    docstring for block CSI_feedback_adapter_py
    """

    binary_byte_read = 8
    channel_est_antennas = []
    file_path = ""

    def __init__(self, file_path):
        gr.basic_block.__init__(self,
            name="CSI_feedback_adapter_py",
            in_sig=None,
            out_sig=None)

        # Input message port
        self.message_port_register_in(pmt.intern("read_file"))

        self.message_port_register_out(pmt.intern("beamweight"))
        self.set_msg_handler(pmt.intern("read_file"), self.send_beamweight)

        self.file_path = file_path

    def send_beamweight(self, msg):

        # Extracting the real and imaginary values of channel estimation
        # First 8 bytes of binary file 'weights_tx2.bin' contain real values
        # Second 8 bytes of binary file 'weights_tx2.bin' contain imaginary values
        # Third 8 bytes of binary file 'weights_tx2.bin' contain the time correction value.
        sbet_file = open(self.file_path + 'weights_tx2.bin')
        sbet_data = sbet_file.read()
        real = struct.unpack('d', sbet_data[0:self.binary_byte_read])[0]
        # print(real)
        imaginary = struct.unpack('d', sbet_data[self.binary_byte_read:2*self.binary_byte_read])[0]
        # print(imaginary)
        time_correct = struct.unpack('d', sbet_data[2*self.binary_byte_read:3*self.binary_byte_read])[0]
        # print(time_correct)

        # Reconstructing channel estimation value in complex format
        # self.channel_est = [real, imaginary]
        channel_est_complex = complex(real, imaginary)

        weight = pmt.from_complex(channel_est_complex)
        self.message_port_pub(pmt.intern("beamweight"), weight)

    def forecast(self, noutput_items, ninput_items_required):
        print("@CSI_feedback_adapter_py:forecast - This function should not be called")


    def general_work(self, input_items, output_items):
        print("@CSI_feedback_adapter_py:general_work - This function should not be called")
        return 0
