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

class multiply_by_variable_py_cc(gr.sync_block):
    """
    docstring for block multiply_by_variable_py_cc
    """

    multiple = 0
    def __init__(self):
        gr.sync_block.__init__(self,
            name="multiply_by_variable_py_cc",
            in_sig=[numpy.complex64],
            out_sig=[numpy.complex64])

        self.multiple = numpy.complex64(complex(1, 1))

        # Input message port
        self.message_port_register_in(pmt.intern("beamweight"))
        self.set_msg_handler(pmt.intern("beamweight"), self.update_multiple)


    def update_multiple(self, msg):
        self.multiple = numpy.complex64(pmt.to_complex(msg))
        #print(self.multiple)

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>
        # print("Input:{} Weight:{} Output:{} \n".format(in0, self.multiple, in0*self.multiple))

        out[:] = in0*self.multiple
        return len(output_items[0])
