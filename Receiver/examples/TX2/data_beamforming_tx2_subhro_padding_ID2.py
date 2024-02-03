#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Data Beamforming Tx2
# Generated: Thu Mar  7 11:56:03 2019
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from optparse import OptionParser
import beamforming
import cons_config  # embedded python module
import pmt
import time
import sys
import wx
import os, threading
import ntplib
import subprocess

class data_beamforming_tx2(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Data Beamforming Tx2")

        ##################################################
        # Variables
        ##################################################
        self.tx_id_1 = tx_id_1 = 2
        self.tx_id_0 = tx_id_0 = 1
        self.trainingSignal_size = trainingSignal_size = 16456
        self.subcarrier_size = subcarrier_size = 1
        self.samp_rate = samp_rate = 400e3
        self.num_active_mod = num_active_mod = 6
        self.numTxAntennas = numTxAntennas = 1
        self.N_edge_zeros = N_edge_zeros = 4
        self.NFFT = NFFT = 256

        ##################################################
        # Blocks
        ##################################################
        self.zero_padding_0_0_0_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self.zero_padding = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("serial=30BC5F6", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_clock_source('external', 0)
        self.uhd_usrp_sink_0.set_time_source('external', 0)
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_time_unknown_pps(uhd.time_spec())
        self.uhd_usrp_sink_0.set_center_freq(uhd.tune_request(900e6, -1e6), 0)
        self.uhd_usrp_sink_0.set_gain(80, 0)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 0)
        self.uhd_usrp_sink_0.set_bandwidth(400e3, 0)
        self.fft_vxx_0 = fft.fft_vcc(NFFT, False, (()), False, 1)
        self.digital_chunks_to_symbols_xx_0_0_1_0_1 = digital.chunks_to_symbols_bc((cons_config.get_points("64QAM")), 1)
        self.digital_chunks_to_symbols_xx_0_0_1_0_0 = digital.chunks_to_symbols_bc((cons_config.get_points("32QAM")), 1)
        self.digital_chunks_to_symbols_xx_0_0_1_0 = digital.chunks_to_symbols_bc((cons_config.get_points("BPSK")), 1)
        self.digital_chunks_to_symbols_xx_0_0_1 = digital.chunks_to_symbols_bc((cons_config.get_points("QPSK")), 1)
        self.digital_chunks_to_symbols_xx_0_0_0 = digital.chunks_to_symbols_bc((cons_config.get_points("16QAM")), 1)
        self.digital_chunks_to_symbols_xx_0_0 = digital.chunks_to_symbols_bc((cons_config.get_points("8QAM")), 1)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, NFFT)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, NFFT)
        self.blocks_stream_mux_1_1 = blocks.stream_mux(gr.sizeof_gr_complex*1, (trainingSignal_size, 400 , NFFT * 64 , 100))
        self.blocks_stream_mux_1_0 = blocks.stream_mux(gr.sizeof_gr_complex*1, (N_edge_zeros, subcarrier_size*num_active_mod, NFFT -num_active_mod - N_edge_zeros))
        self.blocks_stream_mux_0 = blocks.stream_mux(gr.sizeof_gr_complex*1, (1, 1, 1, 1, 1, 1))
        self.blocks_repeat_0_0_0_1_1 = blocks.repeat(gr.sizeof_gr_complex*1, 100 )
        self.blocks_repeat_0_0_0_1_0_0 = blocks.repeat(gr.sizeof_gr_complex*1, 400)
        self.blocks_repeat_0_0_0_0 = blocks.repeat(gr.sizeof_gr_complex*1, subcarrier_size)
        self.blocks_repeat_0_0_0 = blocks.repeat(gr.sizeof_gr_complex*1, NFFT - N_edge_zeros - (num_active_mod*subcarrier_size))
        self.blocks_repeat_0_0 = blocks.repeat(gr.sizeof_gr_complex*1, N_edge_zeros)
        self.blocks_repack_bits_bb_0_1_1_0 = blocks.repack_bits_bb(8, 6, 'packet_len', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0_1_1 = blocks.repack_bits_bb(8, 5, 'packet_len', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0_1_0 = blocks.repack_bits_bb(8, 1, 'packet_len', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0_1 = blocks.repack_bits_bb(8, 2, 'packet_len', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0_0 = blocks.repack_bits_bb(8, 4, 'packet_len', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(8, 3, 'packet_len', False, gr.GR_MSB_FIRST)
        self.blocks_pdu_to_tagged_stream_0_1_2 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'packet_len')
        self.blocks_pdu_to_tagged_stream_0_1_1 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'packet_len')
        self.blocks_pdu_to_tagged_stream_0_1_0 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'packet_len')
        self.blocks_pdu_to_tagged_stream_0_1 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'packet_len')
        self.blocks_pdu_to_tagged_stream_0_0 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'packet_len')
        self.blocks_pdu_to_tagged_stream_0 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'packet_len')
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((0.00390625, ))
        self.blocks_message_strobe_0 = blocks.message_strobe(pmt.PMT_T, 70)
        self.beamforming_payload_generator_cpp_0 = beamforming.payload_generator_cpp('currently_not_used', 1)
        self.beamforming_multiply_by_variable_py_cc_1_0 = beamforming.multiply_by_variable_py_cc()
        self.beamforming_matlab_file_payload_py_0_0 = beamforming.matlab_file_payload_py('/home/nvidia/workarea-gnuradio/gnuradio/gr-beamforming/examples/data/trainingSig2')
        self.beamforming_dynamic_padder_py_0 = beamforming.dynamic_padder_py(0, 0)
        self.beamforming_CSI_feedback_adapter_py_0_0 = beamforming.CSI_feedback_adapter_py(
              1,
              '/home/subhramoy/Documents/test_BF/',
              numTxAntennas,
              '224.3.29.71',
              10000,
              tx_id_1)




        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.beamforming_CSI_feedback_adapter_py_0_0, 'delay'), (self.beamforming_dynamic_padder_py_0, 'trigger'))
        self.msg_connect((self.beamforming_CSI_feedback_adapter_py_0_0, 'beamweight'), (self.beamforming_multiply_by_variable_py_cc_1_0, 'beamweight'))
        self.msg_connect((self.beamforming_payload_generator_cpp_0, '8QAM_pdu'), (self.blocks_pdu_to_tagged_stream_0, 'pdus'))
        self.msg_connect((self.beamforming_payload_generator_cpp_0, '16QAM_pdu'), (self.blocks_pdu_to_tagged_stream_0_0, 'pdus'))
        self.msg_connect((self.beamforming_payload_generator_cpp_0, 'QPSK_pdu'), (self.blocks_pdu_to_tagged_stream_0_1, 'pdus'))
        self.msg_connect((self.beamforming_payload_generator_cpp_0, 'BPSK_pdu'), (self.blocks_pdu_to_tagged_stream_0_1_0, 'pdus'))
        self.msg_connect((self.beamforming_payload_generator_cpp_0, '32QAM_pdu'), (self.blocks_pdu_to_tagged_stream_0_1_1, 'pdus'))
        self.msg_connect((self.beamforming_payload_generator_cpp_0, '64QAM_pdu'), (self.blocks_pdu_to_tagged_stream_0_1_2, 'pdus'))
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.beamforming_CSI_feedback_adapter_py_0_0, 'trigger'))
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.beamforming_payload_generator_cpp_0, 'generate'))
        self.connect((self.beamforming_dynamic_padder_py_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.beamforming_matlab_file_payload_py_0_0, 0), (self.blocks_stream_mux_1_1, 0))
        self.connect((self.beamforming_multiply_by_variable_py_cc_1_0, 0), (self.blocks_stream_mux_1_1, 2))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.beamforming_multiply_by_variable_py_cc_1_0, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_0, 0), (self.blocks_repack_bits_bb_0, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_0_0, 0), (self.blocks_repack_bits_bb_0_0, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_0_1, 0), (self.blocks_repack_bits_bb_0_1, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_0_1_0, 0), (self.blocks_repack_bits_bb_0_1_0, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_0_1_1, 0), (self.blocks_repack_bits_bb_0_1_1, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_0_1_2, 0), (self.blocks_repack_bits_bb_0_1_1_0, 0))
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.digital_chunks_to_symbols_xx_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0, 0), (self.digital_chunks_to_symbols_xx_0_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_1, 0), (self.digital_chunks_to_symbols_xx_0_0_1, 0))
        self.connect((self.blocks_repack_bits_bb_0_1_0, 0), (self.digital_chunks_to_symbols_xx_0_0_1_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_1_1, 0), (self.digital_chunks_to_symbols_xx_0_0_1_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_1_1_0, 0), (self.digital_chunks_to_symbols_xx_0_0_1_0_1, 0))
        self.connect((self.blocks_repeat_0_0, 0), (self.blocks_stream_mux_1_0, 0))
        self.connect((self.blocks_repeat_0_0_0, 0), (self.blocks_stream_mux_1_0, 2))
        self.connect((self.blocks_repeat_0_0_0_0, 0), (self.blocks_stream_mux_1_0, 1))
        self.connect((self.blocks_repeat_0_0_0_1_0_0, 0), (self.blocks_stream_mux_1_1, 1))
        self.connect((self.blocks_repeat_0_0_0_1_1, 0), (self.blocks_stream_mux_1_1, 3))
        self.connect((self.blocks_stream_mux_0, 0), (self.blocks_repeat_0_0_0_0, 0))
        self.connect((self.blocks_stream_mux_1_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.blocks_stream_mux_1_1, 0), (self.beamforming_dynamic_padder_py_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.blocks_vector_to_stream_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0_0, 0), (self.blocks_stream_mux_0, 3))
        self.connect((self.digital_chunks_to_symbols_xx_0_0_0, 0), (self.blocks_stream_mux_0, 2))
        self.connect((self.digital_chunks_to_symbols_xx_0_0_1, 0), (self.blocks_stream_mux_0, 4))
        self.connect((self.digital_chunks_to_symbols_xx_0_0_1_0, 0), (self.blocks_stream_mux_0, 5))
        self.connect((self.digital_chunks_to_symbols_xx_0_0_1_0_0, 0), (self.blocks_stream_mux_0, 1))
        self.connect((self.digital_chunks_to_symbols_xx_0_0_1_0_1, 0), (self.blocks_stream_mux_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_vector_to_stream_0, 0))
        self.connect((self.zero_padding, 0), (self.blocks_repeat_0_0, 0))
        self.connect((self.zero_padding, 0), (self.blocks_repeat_0_0_0, 0))
        self.connect((self.zero_padding_0_0_0_0, 0), (self.blocks_repeat_0_0_0_1_0_0, 0))
        self.connect((self.zero_padding_0_0_0_0, 0), (self.blocks_repeat_0_0_0_1_1, 0))


	##################################################
	# Adding line for time sync purpose
	##################################################
#	try:
	lock = threading.Lock()
	lock.acquire()

	client = ntplib.NTPClient()
	response = client.request('10.42.0.1')
	#response = client.request('pool.ntp.org')
	os.system('date ' + time.strftime('%m%d%H%M%Y.%S',time.localtime(response.tx_time)))
	
	#os.system(time.strftime('%m%d%H%M%Y.%S',time.localtime(response.tx_time)))
	system_time_min = int(time.strftime('%M'))
	system_time_min = (system_time_min*60)
        
	print (system_time_min)
        system_time_sec = int(time.strftime('%S'))
        print (system_time_sec)
        system_time_str = (system_time_min + system_time_sec)
	wait_time = 60 - system_time_sec
	print "Tranmission will start after {} seconds".format(wait_time)
	print(system_time_str) 
        system_time = int(system_time_str)
	#self.uhd_usrp_sink_0.set_time_unknown_pps(uhd.time_spec_t(system_time +1))	
	self.uhd_usrp_sink_0.set_time_next_pps(uhd.time_spec_t(system_time +1))
	self.uhd_usrp_sink_0.set_start_time(uhd.time_spec_t(system_time + wait_time))
	print "wait over"
	lock.release()
	time.sleep(wait_time-2)

	##################################################
	# Other functions
	##################################################


    def get_tx_id_1(self):
        return self.tx_id_1

    def set_tx_id_1(self, tx_id_1):
        self.tx_id_1 = tx_id_1

    def get_tx_id_0(self):
        return self.tx_id_0

    def set_tx_id_0(self, tx_id_0):
        self.tx_id_0 = tx_id_0

    def get_trainingSignal_size(self):
        return self.trainingSignal_size

    def set_trainingSignal_size(self, trainingSignal_size):
        self.trainingSignal_size = trainingSignal_size

    def get_subcarrier_size(self):
        return self.subcarrier_size

    def set_subcarrier_size(self, subcarrier_size):
        self.subcarrier_size = subcarrier_size
        self.blocks_repeat_0_0_0_0.set_interpolation(self.subcarrier_size)
        self.blocks_repeat_0_0_0.set_interpolation(self.NFFT - self.N_edge_zeros - (self.num_active_mod*self.subcarrier_size))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)

    def get_num_active_mod(self):
        return self.num_active_mod

    def set_num_active_mod(self, num_active_mod):
        self.num_active_mod = num_active_mod
        self.blocks_repeat_0_0_0.set_interpolation(self.NFFT - self.N_edge_zeros - (self.num_active_mod*self.subcarrier_size))

    def get_numTxAntennas(self):
        return self.numTxAntennas

    def set_numTxAntennas(self, numTxAntennas):
        self.numTxAntennas = numTxAntennas
        self.blocks_repeat_0_0_0_1_1.set_interpolation(100 )
        self.blocks_repeat_0_0_0_1_0_0.set_interpolation(400)

    def get_N_edge_zeros(self):
        return self.N_edge_zeros

    def set_N_edge_zeros(self, N_edge_zeros):
        self.N_edge_zeros = N_edge_zeros
        self.blocks_repeat_0_0_0.set_interpolation(self.NFFT - self.N_edge_zeros - (self.num_active_mod*self.subcarrier_size))
        self.blocks_repeat_0_0.set_interpolation(self.N_edge_zeros)

    def get_NFFT(self):
        return self.NFFT

    def set_NFFT(self, NFFT):
        self.NFFT = NFFT
        self.blocks_repeat_0_0_0.set_interpolation(self.NFFT - self.N_edge_zeros - (self.num_active_mod*self.subcarrier_size))


def main(top_block_cls=data_beamforming_tx2, options=None):

    tb = top_block_cls()
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
