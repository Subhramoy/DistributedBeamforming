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

import numpy
from gnuradio import gr
import numpy
import pmt

class dynamic_padder_py(gr.basic_block):
    """
    docstring for block dynamic_padder_py
    """
    def __init__(self, real, imag):
        gr.basic_block.__init__(self,
            name="dynamic_padder_py",
            in_sig=[numpy.complex64],
            out_sig=[numpy.complex64])


        complex_value = complex(float(real) ,float(imag))
        self.padding_sample = numpy.complex64(complex_value)
        print "Recevied sample: {}".format(self.padding_sample)

        self.padding = False

        # Init input message port
        self.message_port_register_in(pmt.intern("trigger"))
        self.set_msg_handler(pmt.intern("trigger"), self.set_padding)

    def forecast(self, noutput_items, ninput_items_required):
        print "forecast called noutput_items:{}".format(noutput_items)
        #setup size of input_items[i] for work call
        for i in range(len(ninput_items_required)):
            ninput_items_required[i] = noutput_items

    def general_work(self, input_items, output_items):
        print "General work called in:{} - out:{}".format(len(input_items[0]), len(output_items[0]))

        if self.padding is True:
            sub_input = input_items[0][:len(output_items[0]) -self.length ]

            output = numpy.append(sub_input, self.get_padding_array(self.length))
            #numpy.append (
            #    input_items[0][:len(output_items[0]) -self.length ],
            #    self.get_padding_array(self.length))

#            print output
#            print len(output)
            output_items[0][:] = output
            self.consume(0, len(output_items[0])-self.length)

            self.padding = False
        else:
            output_items[0][:] = input_items[0][:len(output_items[0])]
            self.consume(0, len(output_items[0]))
            #self.consume_each(len(input_items[0]))

        return len(output_items[0])

    def set_padding(self, msg):

        self.length = int(pmt.symbol_to_string(msg))

        print(self.length)
        self.padding = True


    def get_padding_array(self, length):
        index = 0
        payload = []

        while index < length:
            payload.append(self.padding_sample)
            index = index +1

        return payload
