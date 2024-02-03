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

from gnuradio import gr, gr_unittest
from gnuradio import blocks
from matlab_file_payload_py import matlab_file_payload_py
import numpy

class qa_matlab_file_payload_py (gr_unittest.TestCase):

    # File path to read IQ samples
    file_path = "/home/gokhan/gnu-radio/gr-beamforming/examples/data/trainingSig1"
    expected_payload = []

    def setUp (self):
        self.tb = gr.top_block ()

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
            self.expected_payload.append(data)

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        # set up fg
        self.tb.matlab_file_pL_module = matlab_file_payload_py(self.file_path)
        dst = blocks.vector_sink_c()
        self.tb.connect(self.tb.matlab_file_pL_module, dst)

        self.tb.run()
        self.tb.stop()
        # check data
        result_data = dst.data()
        print(result_data)

        #self.assertFloatTuplesAlmostEqual(self.expected_payload, result_data, 6)



if __name__ == '__main__':
    gr_unittest.run(qa_matlab_file_payload_py, "qa_matlab_file_payload_py.xml")
