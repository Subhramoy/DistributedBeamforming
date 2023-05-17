#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2018 GENESYS.
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
from gnuradio import blocks

class payloadSource(gr.basic_block):
    """
    docstring for block payloadSource
    """
    def __init__(self, file_path, size):
        gr.basic_block.__init__(self,
                                name="payloadSource",
                                in_sig=None,
                                out_sig=None)
        print("So far so good")

        # Input message port
        self.message_port_register_in(pmt.intern("generate"))

        # Output message ports
        self.message_port_register_out(pmt.intern("64QAM_pdu"))
        self.message_port_register_out(pmt.intern("32QAM_pdu"))
        self.message_port_register_out(pmt.intern("16QAM_pdu"))
        self.message_port_register_out(pmt.intern("8QAM_pdu"))
        self.message_port_register_out(pmt.intern("QPSK_pdu"))
        self.message_port_register_out(pmt.intern("BSPK_pdu"))

        self.set_msg_handler(pmt.intern("generate"), self.handle_msg)

    def handle_msg(self, msg):
        print("Generating Packet")
        print(pmt.is_symbol(pmt.intern("0010 0000")))
        print(pmt.is_vector(pmt.intern("0010 0000")))

        value = pmt.from_long(1)
        print(type(value))

        vector = pmt.make_vector(1, value)
        print(pmt.is_vector(vector))


        print (type(ptr))

        blob = pmt.make_blob(ptr,64)
        print (type(blob))


        # // fill it with random bytes
        # std::vector<unsigned char> vec(len);
        # for (int i=0; i<len; i++)
        #     vec[i] = ((unsigned char) d_bvar()) & d_mask;
        #
        # // send the vector
        # pmt::pmt_t vecpmt(pmt::make_blob(&vec[0], len));
        # pmt::pmt_t pdu(pmt::cons(pmt::PMT_NIL, vecpmt));

        # message_port_pub(pdu::pdu_port_id(), pdu);


        self.message_port_pub(pmt.intern("64QAM_pdu"), vector)
        self.message_port_pub(pmt.intern("32QAM_pdu"), pmt.intern("0010 0000"))
        self.message_port_pub(pmt.intern("16QAM_pdu"), pmt.intern("0001 0000"))
        self.message_port_pub(pmt.intern("8QAM_pdu"), pmt.intern("0000 1000"))
        self.message_port_pub(pmt.intern("QPSK_pdu"), pmt.intern("0000 0100"))
        self.message_port_pub(pmt.intern("BSPK_pdu"), pmt.intern("0000 0010"))




    def forecast(self, noutput_items, ninput_items_required):
        print("@payloadSource:forecast - This function should not be called")
        #setup size of input_items[i] for work call
        for i in range(len(ninput_items_required)):
            ninput_items_required[i] = noutput_items

    def general_work(self, input_items, output_items):
        print("@payloadSource:general_work - This function should not be called")
        output_items[0][:] = input_items[0]
        consume(0, len(input_items[0]))
        #self.consume_each(len(input_items[0]))
        return len(output_items[0])


