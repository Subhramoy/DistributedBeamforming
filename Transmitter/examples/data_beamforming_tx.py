#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Data Beamforming Tx
# Generated: Mon Jan 14 14:40:07 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from optparse import OptionParser
import beamforming
import cons_config  # embedded python module
import pmt
import sip
import sys
from gnuradio import qtgui


class data_beamforming_tx(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Data Beamforming Tx")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Data Beamforming Tx")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "data_beamforming_tx")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.trainingSignal_size = trainingSignal_size = 16456
        self.subcarrier_size = subcarrier_size = 19
        self.num_active_mod = num_active_mod = 6
        self.numTxAntennas = numTxAntennas = 1
        self.N_edge_zeros = N_edge_zeros = 3
        self.N_center_zeros = N_center_zeros = 11
        self.NFFT = NFFT = 256

        ##################################################
        # Blocks
        ##################################################
        self.zero_padding_0_0_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self.zero_padding_0_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self.zero_padding_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self.zero_padding = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self.qtgui_time_sink_x_0_0_1_1_0 = qtgui.time_sink_c(
        	1024*64, #size
        	100000, #samp_rate
        	"Training+Payload", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_1_1_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_1_1_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0_1_1_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_1_1_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_1_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_1_1_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_1_1_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_1_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_1_1_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_1_1_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0_1_1_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0_0_1_1_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_0_1_1_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_0_1_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_1_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_1_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_1_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_1_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_1_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_1_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_1_1_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_1_1_0_win)
        self.qtgui_time_sink_x_0_0_1_1 = qtgui.time_sink_c(
        	1024, #size
        	400e3, #samp_rate
        	"Payload", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_1_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_1_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0_1_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_1_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_1_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_1_1.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0_1_1.enable_grid(False)
        self.qtgui_time_sink_x_0_0_1_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_1_1.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_1_1.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0_1_1.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0_0_1_1.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_0_1_1.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_0_1_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_1_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_1_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_1_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_1_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_1_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_1_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_1_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_1_1_win)
        self.qtgui_freq_sink_x_0_0_0 = qtgui.freq_sink_c(
        	NFFT*16, #size
        	firdes.WIN_FLATTOP, #wintype
        	0, #fc
        	200000, #bw
        	'FFT Plot', #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_0_win)
        self.fft_vxx_0 = fft.fft_vcc(NFFT, False, (()), False, 1)
        self.digital_chunks_to_symbols_xx_0_0_1_0_1 = digital.chunks_to_symbols_bc((cons_config.get_points("64QAM")), 1)
        self.digital_chunks_to_symbols_xx_0_0_1_0_0 = digital.chunks_to_symbols_bc((cons_config.get_points("32QAM")), 1)
        self.digital_chunks_to_symbols_xx_0_0_1_0 = digital.chunks_to_symbols_bc((cons_config.get_points("BPSK")), 1)
        self.digital_chunks_to_symbols_xx_0_0_1 = digital.chunks_to_symbols_bc((cons_config.get_points("QPSK")), 1)
        self.digital_chunks_to_symbols_xx_0_0_0 = digital.chunks_to_symbols_bc((cons_config.get_points("16QAM")), 1)
        self.digital_chunks_to_symbols_xx_0_0 = digital.chunks_to_symbols_bc((cons_config.get_points("8QAM")), 1)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, NFFT)
        self.blocks_tag_gate_0 = blocks.tag_gate(gr.sizeof_gr_complex * 1, False)
        self.blocks_tag_gate_0.set_single_key("packet_len")
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, NFFT)
        self.blocks_stream_mux_1_0 = blocks.stream_mux(gr.sizeof_gr_complex*1, (N_edge_zeros, num_active_mod*subcarrier_size,N_center_zeros, num_active_mod*subcarrier_size, N_center_zeros, N_edge_zeros))
        self.blocks_stream_mux_1 = blocks.stream_mux(gr.sizeof_gr_complex*1, (trainingSignal_size, 400, NFFT * 64 , 100))
        self.blocks_stream_mux_0 = blocks.stream_mux(gr.sizeof_gr_complex*1, (1, 1, 1, 1, 1, 1))
        self.blocks_repeat_0_0_0_1_0 = blocks.repeat(gr.sizeof_gr_complex*1, 400 * numTxAntennas)
        self.blocks_repeat_0_0_0_1 = blocks.repeat(gr.sizeof_gr_complex*1, 100 * numTxAntennas)
        self.blocks_repeat_0_0_0 = blocks.repeat(gr.sizeof_gr_complex*1, N_center_zeros)
        self.blocks_repeat_0_0 = blocks.repeat(gr.sizeof_gr_complex*1, N_edge_zeros)
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_gr_complex*1, subcarrier_size)
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
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((-390625e-8, ))
        self.blocks_message_strobe_0 = blocks.message_strobe(pmt.PMT_T, 200)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, '/home/gokhan/gnu-radio/gr-beamforming/examples/payload-afterWeight.bin', False)
        self.blocks_file_sink_0.set_unbuffered(True)
        self.beamforming_payload_generator_cpp_0 = beamforming.payload_generator_cpp('currently_not_used', 1)
        self.beamforming_multiply_by_variable_py_cc_1 = beamforming.multiply_by_variable_py_cc()
        self.beamforming_matlab_file_payload_py_0 = beamforming.matlab_file_payload_py('/home/gokhan/gnu-radio/gr-beamforming/examples/data/trainingSig1')
        self.beamforming_CSI_feedback_adapter_py_0 = beamforming.CSI_feedback_adapter_py('/home/gokhan/gnu-radio/gr-beamforming/examples/data/weights_tx2.bin', 1, '224.3.29.71', '10000', '1')



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.beamforming_CSI_feedback_adapter_py_0, 'beamweight'), (self.beamforming_multiply_by_variable_py_cc_1, 'beamweight'))
        self.msg_connect((self.beamforming_payload_generator_cpp_0, '8QAM_pdu'), (self.blocks_pdu_to_tagged_stream_0, 'pdus'))
        self.msg_connect((self.beamforming_payload_generator_cpp_0, '16QAM_pdu'), (self.blocks_pdu_to_tagged_stream_0_0, 'pdus'))
        self.msg_connect((self.beamforming_payload_generator_cpp_0, 'QPSK_pdu'), (self.blocks_pdu_to_tagged_stream_0_1, 'pdus'))
        self.msg_connect((self.beamforming_payload_generator_cpp_0, 'BPSK_pdu'), (self.blocks_pdu_to_tagged_stream_0_1_0, 'pdus'))
        self.msg_connect((self.beamforming_payload_generator_cpp_0, '32QAM_pdu'), (self.blocks_pdu_to_tagged_stream_0_1_1, 'pdus'))
        self.msg_connect((self.beamforming_payload_generator_cpp_0, '64QAM_pdu'), (self.blocks_pdu_to_tagged_stream_0_1_2, 'pdus'))
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.beamforming_CSI_feedback_adapter_py_0, 'trigger'))
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.beamforming_payload_generator_cpp_0, 'generate'))
        self.connect((self.beamforming_matlab_file_payload_py_0, 0), (self.blocks_stream_mux_1, 0))
        self.connect((self.beamforming_multiply_by_variable_py_cc_1, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.beamforming_multiply_by_variable_py_cc_1, 0), (self.blocks_stream_mux_1, 2))
        self.connect((self.beamforming_multiply_by_variable_py_cc_1, 0), (self.qtgui_time_sink_x_0_0_1_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.beamforming_multiply_by_variable_py_cc_1, 0))
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
        self.connect((self.blocks_repeat_0, 0), (self.blocks_stream_mux_1_0, 1))
        self.connect((self.blocks_repeat_0, 0), (self.blocks_stream_mux_1_0, 3))
        self.connect((self.blocks_repeat_0_0, 0), (self.blocks_stream_mux_1_0, 0))
        self.connect((self.blocks_repeat_0_0, 0), (self.blocks_stream_mux_1_0, 5))
        self.connect((self.blocks_repeat_0_0_0, 0), (self.blocks_stream_mux_1_0, 2))
        self.connect((self.blocks_repeat_0_0_0, 0), (self.blocks_stream_mux_1_0, 4))
        self.connect((self.blocks_repeat_0_0_0_1, 0), (self.blocks_stream_mux_1, 3))
        self.connect((self.blocks_repeat_0_0_0_1_0, 0), (self.blocks_stream_mux_1, 1))
        self.connect((self.blocks_stream_mux_0, 0), (self.blocks_tag_gate_0, 0))
        self.connect((self.blocks_stream_mux_1, 0), (self.qtgui_freq_sink_x_0_0_0, 0))
        self.connect((self.blocks_stream_mux_1, 0), (self.qtgui_time_sink_x_0_0_1_1_0, 0))
        self.connect((self.blocks_stream_mux_1_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.blocks_tag_gate_0, 0), (self.blocks_repeat_0, 0))
        self.connect((self.blocks_vector_to_stream_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0_0, 0), (self.blocks_stream_mux_0, 3))
        self.connect((self.digital_chunks_to_symbols_xx_0_0_0, 0), (self.blocks_stream_mux_0, 2))
        self.connect((self.digital_chunks_to_symbols_xx_0_0_1, 0), (self.blocks_stream_mux_0, 4))
        self.connect((self.digital_chunks_to_symbols_xx_0_0_1_0, 0), (self.blocks_stream_mux_0, 5))
        self.connect((self.digital_chunks_to_symbols_xx_0_0_1_0_0, 0), (self.blocks_stream_mux_0, 1))
        self.connect((self.digital_chunks_to_symbols_xx_0_0_1_0_1, 0), (self.blocks_stream_mux_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_vector_to_stream_0, 0))
        self.connect((self.zero_padding, 0), (self.blocks_repeat_0_0, 0))
        self.connect((self.zero_padding_0, 0), (self.blocks_repeat_0_0_0, 0))
        self.connect((self.zero_padding_0_0, 0), (self.blocks_repeat_0_0_0_1, 0))
        self.connect((self.zero_padding_0_0_0, 0), (self.blocks_repeat_0_0_0_1_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "data_beamforming_tx")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_trainingSignal_size(self):
        return self.trainingSignal_size

    def set_trainingSignal_size(self, trainingSignal_size):
        self.trainingSignal_size = trainingSignal_size

    def get_subcarrier_size(self):
        return self.subcarrier_size

    def set_subcarrier_size(self, subcarrier_size):
        self.subcarrier_size = subcarrier_size
        self.blocks_repeat_0.set_interpolation(self.subcarrier_size)

    def get_num_active_mod(self):
        return self.num_active_mod

    def set_num_active_mod(self, num_active_mod):
        self.num_active_mod = num_active_mod

    def get_numTxAntennas(self):
        return self.numTxAntennas

    def set_numTxAntennas(self, numTxAntennas):
        self.numTxAntennas = numTxAntennas
        self.blocks_repeat_0_0_0_1_0.set_interpolation(400 * self.numTxAntennas)
        self.blocks_repeat_0_0_0_1.set_interpolation(100 * self.numTxAntennas)

    def get_N_edge_zeros(self):
        return self.N_edge_zeros

    def set_N_edge_zeros(self, N_edge_zeros):
        self.N_edge_zeros = N_edge_zeros
        self.blocks_repeat_0_0.set_interpolation(self.N_edge_zeros)

    def get_N_center_zeros(self):
        return self.N_center_zeros

    def set_N_center_zeros(self, N_center_zeros):
        self.N_center_zeros = N_center_zeros
        self.blocks_repeat_0_0_0.set_interpolation(self.N_center_zeros)

    def get_NFFT(self):
        return self.NFFT

    def set_NFFT(self, NFFT):
        self.NFFT = NFFT


def main(top_block_cls=data_beamforming_tx, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
