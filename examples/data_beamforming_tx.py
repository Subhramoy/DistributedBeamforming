#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Data Beamforming Tx
# Generated: Wed Oct 24 11:42:12 2018
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
import numpy
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
        self.sync_word2 = sync_word2 = [0, 0, 0, 0, 0, 0, -1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, 0, 1, -1, 1, 1, 1, -1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1, -1, -1, 0, 0, 0, 0, 0]
        self.sync_word1 = sync_word1 = [0., 0., 0., 0., 0., 0., 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 0., 0., 0., 0., 0.]
        self.subcarrier_size = subcarrier_size = 1
        self.q_8QAM = q_8QAM = digital.constellation_rect(([-1-1j, -1+0j, -1+1j, 0-1j, 0+1j, 1+-1j, 1+0j, 1+1j ]), ([0, 1, 2, 3, 4, 5, 6, 7]), 4, 3, 3, 1, 1).base()
        self.pilot_symbols = pilot_symbols = ((1, 1, 1, -1,),)
        self.pilot_carriers = pilot_carriers = (  range(-20, -7) + range(-6, 0) + range(1, 7) + range(8, 21) + range(22, 27), )

        self.payload_QPSK = payload_QPSK = digital.constellation_qpsk().base()

        self.payload_QPSK.gen_soft_dec_lut(8)

        self.payload_8QAM = payload_8QAM = digital.constellation_8psk().base()

        self.payload_8QAM.gen_soft_dec_lut(8)

        self.payload_16QAM = payload_16QAM = digital.constellation_16qam().base()

        self.payload_16QAM.gen_soft_dec_lut(8)
        self.occupied_carriers = occupied_carriers = (range(-26, -21) ,)
        self.num_active_mod = num_active_mod = 6
        self.QPSK = QPSK = digital.constellation_rect(([-1-1j, -1+1j, 1+1j, 1-1j]), ([0, 1, 2, 3]), 4, 2, 2, 1, 1).base()
        self.N_edge_zeros = N_edge_zeros = 1
        self.N_center_zeros = N_center_zeros = 1
        self.NFFT = NFFT = 256

        ##################################################
        # Blocks
        ##################################################
        self.zero_padding_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self.zero_padding = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self.qtgui_time_sink_x_0_0_1_1 = qtgui.time_sink_c(
        	1024, #size
        	100000, #samp_rate
        	"Time Plot", #name
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
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	NFFT *8, #size
        	firdes.WIN_FLATTOP, #wintype
        	900000000, #fc
        	200000, #bw
        	'FFT Plot', #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0.set_plot_pos_half(not True)

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
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_win)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_win)
        self.fft_vxx_0 = fft.fft_vcc(NFFT, False, (()), False, 1)
        self.digital_chunks_to_symbols_xx_0_0_1 = digital.chunks_to_symbols_bc((payload_QPSK.points()), 1)
        self.digital_chunks_to_symbols_xx_0_0_0 = digital.chunks_to_symbols_bc((payload_16QAM.points()), 1)
        self.digital_chunks_to_symbols_xx_0_0 = digital.chunks_to_symbols_bc((payload_8QAM.points()), 1)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, NFFT)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, 100000,True)
        self.blocks_tagged_stream_mux_0 = blocks.tagged_stream_mux(gr.sizeof_gr_complex*1, "sym_len", 0)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, NFFT)
        self.blocks_stream_to_tagged_stream_1 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, 64, "packet_len")
        self.blocks_stream_to_tagged_stream_0_1 = blocks.stream_to_tagged_stream(gr.sizeof_gr_complex, 1, N_center_zeros, "sym_len")
        self.blocks_stream_to_tagged_stream_0_0 = blocks.stream_to_tagged_stream(gr.sizeof_gr_complex, 1, N_edge_zeros, "sym_len")
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_gr_complex, 1, subcarrier_size * num_active_mod, "sym_len")
        self.blocks_stream_mux_0 = blocks.stream_mux(gr.sizeof_gr_complex*1, (1, 1, 1, 1, 1, 1))
        self.blocks_repeat_0_0_0 = blocks.repeat(gr.sizeof_gr_complex*1, N_center_zeros)
        self.blocks_repeat_0_0 = blocks.repeat(gr.sizeof_gr_complex*1, N_edge_zeros)
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_gr_complex*1, subcarrier_size)
        self.blocks_repack_bits_bb_0_1 = blocks.repack_bits_bb(8, 2, 'packet_len', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0_0 = blocks.repack_bits_bb(8, 4, 'packet_len', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(8, 3, 'packet_len', False, gr.GR_MSB_FIRST)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((0.2, ))
        self.blocks_message_debug_0 = blocks.message_debug()
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 255, 1000)), True)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_stream_to_tagged_stream_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_time_sink_x_0_0_1_1, 0))
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.digital_chunks_to_symbols_xx_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0, 0), (self.digital_chunks_to_symbols_xx_0_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_1, 0), (self.digital_chunks_to_symbols_xx_0_0_1, 0))
        self.connect((self.blocks_repeat_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))
        self.connect((self.blocks_repeat_0_0, 0), (self.blocks_stream_to_tagged_stream_0_0, 0))
        self.connect((self.blocks_repeat_0_0_0, 0), (self.blocks_stream_to_tagged_stream_0_1, 0))
        self.connect((self.blocks_stream_mux_0, 0), (self.blocks_repeat_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.blocks_tagged_stream_mux_0, 1))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.blocks_tagged_stream_mux_0, 3))
        self.connect((self.blocks_stream_to_tagged_stream_0_0, 0), (self.blocks_tagged_stream_mux_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0_0, 0), (self.blocks_tagged_stream_mux_0, 5))
        self.connect((self.blocks_stream_to_tagged_stream_0_1, 0), (self.blocks_tagged_stream_mux_0, 2))
        self.connect((self.blocks_stream_to_tagged_stream_0_1, 0), (self.blocks_tagged_stream_mux_0, 4))
        self.connect((self.blocks_stream_to_tagged_stream_1, 0), (self.blocks_repack_bits_bb_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_1, 0), (self.blocks_repack_bits_bb_0_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_1, 0), (self.blocks_repack_bits_bb_0_1, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.blocks_tagged_stream_mux_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.blocks_vector_to_stream_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0_0, 0), (self.blocks_stream_mux_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0_0, 0), (self.blocks_stream_mux_0, 3))
        self.connect((self.digital_chunks_to_symbols_xx_0_0_0, 0), (self.blocks_stream_mux_0, 1))
        self.connect((self.digital_chunks_to_symbols_xx_0_0_0, 0), (self.blocks_stream_mux_0, 2))
        self.connect((self.digital_chunks_to_symbols_xx_0_0_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0_0_1, 0), (self.blocks_stream_mux_0, 4))
        self.connect((self.digital_chunks_to_symbols_xx_0_0_1, 0), (self.blocks_stream_mux_0, 5))
        self.connect((self.fft_vxx_0, 0), (self.blocks_vector_to_stream_0, 0))
        self.connect((self.zero_padding, 0), (self.blocks_repeat_0_0, 0))
        self.connect((self.zero_padding_0, 0), (self.blocks_repeat_0_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "data_beamforming_tx")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sync_word2(self):
        return self.sync_word2

    def set_sync_word2(self, sync_word2):
        self.sync_word2 = sync_word2

    def get_sync_word1(self):
        return self.sync_word1

    def set_sync_word1(self, sync_word1):
        self.sync_word1 = sync_word1

    def get_subcarrier_size(self):
        return self.subcarrier_size

    def set_subcarrier_size(self, subcarrier_size):
        self.subcarrier_size = subcarrier_size
        self.blocks_stream_to_tagged_stream_0.set_packet_len(self.subcarrier_size * self.num_active_mod)
        self.blocks_stream_to_tagged_stream_0.set_packet_len_pmt(self.subcarrier_size * self.num_active_mod)
        self.blocks_repeat_0.set_interpolation(self.subcarrier_size)

    def get_q_8QAM(self):
        return self.q_8QAM

    def set_q_8QAM(self, q_8QAM):
        self.q_8QAM = q_8QAM

    def get_pilot_symbols(self):
        return self.pilot_symbols

    def set_pilot_symbols(self, pilot_symbols):
        self.pilot_symbols = pilot_symbols

    def get_pilot_carriers(self):
        return self.pilot_carriers

    def set_pilot_carriers(self, pilot_carriers):
        self.pilot_carriers = pilot_carriers

    def get_payload_QPSK(self):
        return self.payload_QPSK

    def set_payload_QPSK(self, payload_QPSK):
        self.payload_QPSK = payload_QPSK

    def get_payload_8QAM(self):
        return self.payload_8QAM

    def set_payload_8QAM(self, payload_8QAM):
        self.payload_8QAM = payload_8QAM

    def get_payload_16QAM(self):
        return self.payload_16QAM

    def set_payload_16QAM(self, payload_16QAM):
        self.payload_16QAM = payload_16QAM

    def get_occupied_carriers(self):
        return self.occupied_carriers

    def set_occupied_carriers(self, occupied_carriers):
        self.occupied_carriers = occupied_carriers

    def get_num_active_mod(self):
        return self.num_active_mod

    def set_num_active_mod(self, num_active_mod):
        self.num_active_mod = num_active_mod
        self.blocks_stream_to_tagged_stream_0.set_packet_len(self.subcarrier_size * self.num_active_mod)
        self.blocks_stream_to_tagged_stream_0.set_packet_len_pmt(self.subcarrier_size * self.num_active_mod)

    def get_QPSK(self):
        return self.QPSK

    def set_QPSK(self, QPSK):
        self.QPSK = QPSK

    def get_N_edge_zeros(self):
        return self.N_edge_zeros

    def set_N_edge_zeros(self, N_edge_zeros):
        self.N_edge_zeros = N_edge_zeros
        self.blocks_stream_to_tagged_stream_0_0.set_packet_len(self.N_edge_zeros)
        self.blocks_stream_to_tagged_stream_0_0.set_packet_len_pmt(self.N_edge_zeros)
        self.blocks_repeat_0_0.set_interpolation(self.N_edge_zeros)

    def get_N_center_zeros(self):
        return self.N_center_zeros

    def set_N_center_zeros(self, N_center_zeros):
        self.N_center_zeros = N_center_zeros
        self.blocks_stream_to_tagged_stream_0_1.set_packet_len(self.N_center_zeros)
        self.blocks_stream_to_tagged_stream_0_1.set_packet_len_pmt(self.N_center_zeros)
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
