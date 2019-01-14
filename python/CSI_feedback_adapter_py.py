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

#############################
# TO DO List:
# 1- Separate classes into different python files.
# 2-
#
#############################

import struct
import pmt
import numpy
import sys
import math
import cmath
from gnuradio import gr


# UDP related libraries
import socket
import struct
import threading
import time


class CSI_feedback_adapter_py(gr.basic_block):
    """
    docstring for block CSI_feedback_adapter_py
    """

    channel_est_antennas = []
    file_path = ""

    numTxAntennas = 1
    beamweight = complex(1.0, 1.0)

    def __init__(self, file_path, number_of_tx_antennas, multicast_IP, multicast_port, Tx_ID):
        gr.basic_block.__init__(self,
            name="CSI_feedback_adapter_py",
            in_sig=None,
            out_sig=None)

        self.numTxAntennas = number_of_tx_antennas

        # Input message port
        self.message_port_register_in(pmt.intern("trigger"))

        self.message_port_register_out(pmt.intern("beamweight"))
        self.set_msg_handler(pmt.intern("trigger"), self.send_beamweight)

        self.file_path = file_path

        address = multicast_IP, int(multicast_port)
        self.UDP_socket = UDPServer(address, self.udp_packet_handler)
        self.UDP_socket.start()


    def udp_packet_handler(self, json_package):
        print(json_package)


    def send_beamweight(self, msg):
        weight = pmt.from_complex(self.beamweight)
        self.message_port_pub(pmt.intern("beamweight"), weight)


    # Unused function - will be truncated in future
    def read_bw_from_file(self, file_path):
        self.binary_byte_read = 8
        # Extracting the real and imaginary values of channel estimation
        # First 8 bytes of binary file 'weights_tx2.bin' contain real values
        # Second 8 bytes of binary file 'weights_tx2.bin' contain imaginary values
        # Third 8 bytes of binary file 'weights_tx2.bin' contain the time correction value.
        sbet_file = open(file_path)
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
        abs_channel_est_antennas = abs(channel_est_complex)
        phase_correction = channel_est_complex / abs_channel_est_antennas

        beamweight = 1/phase_correction
        return beamweight


    def forecast(self, noutput_items, ninput_items_required):
        print("@CSI_feedback_adapter_py:forecast - This function should not be called")


    def general_work(self, input_items, output_items):
        print("@CSI_feedback_adapter_py:general_work - This function should not be called")
        return 0


class UDPServer(threading.Thread):
    def __init__(self, address, udp_packet_handler):
        print("UDP server generated.")

        self.multicast_group = address[0]
        self.port = address[1]

        self.udp_packet_handler = udp_packet_handler

        threading.Thread.__init__(self)

    def run(self):
        try:
            # Create the socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            # Bind to the server address
            sock.bind(('', self.port))

            # Tell the operating system to add the socket to the multicast group
            # on all interfaces.
            group = socket.inet_aton(self.multicast_group)
            mreq = struct.pack('4sL', group, socket.INADDR_ANY)
            sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

        except socket.error as exp:
            print("Exception while creating the socket\n%s" % exp)
            sock.close()


        # Receive loop
        while True:
            # print >> sys.stderr, '\nwaiting to receive message'
            try:
                data, address = sock.recvfrom(1024)
            except socket.timeout:
                print('timed out, no incoming CSI feedback')
                break
            else:
                print('received "%s" from %s - time: %f ' % (data, address, time.time() ) )
                self.udp_packet_handler(data)


