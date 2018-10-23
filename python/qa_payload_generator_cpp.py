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


import sys
sys.path.append('/usr/local/lib/python2.7/dist-packages/beamforming/')

import pmt
from gnuradio import gr, gr_unittest
from gnuradio import blocks
import beamforming_swig as beamforming

class qa_payload_generator_cpp (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        # set up fg
        self.tb.run ()
        # check data
    def test_002_t (self):
        # set up fg
        self.tb.payload = beamforming.payload_generator_cpp("dummyPath", 1)
        self.tb.blocks_message_strobe_ = blocks.message_strobe(pmt.PMT_T, 2000)
        self.tb.msg_connect((self.tb.blocks_message_strobe_, 'strobe'), (self.tb.payload, 'generate'))
        self.tb.run ()
        # check data


if __name__ == '__main__':
    gr_unittest.run(qa_payload_generator_cpp, "qa_payload_generator_cpp.xml")
