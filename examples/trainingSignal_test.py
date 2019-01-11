#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Trainingsignal Test
# Generated: Fri Jan 11 14:41:20 2019
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
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import beamforming
import sip
import sys
from gnuradio import qtgui


class trainingSignal_test(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Trainingsignal Test")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Trainingsignal Test")
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

        self.settings = Qt.QSettings("GNU Radio", "trainingSignal_test")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 400e3

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_time_sink_x_0_0_1_1_0_0 = qtgui.time_sink_c(
        	4000000, #size
        	400e3, #samp_rate
        	'Tx Signal', #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_1_1_0_0.set_update_time(1.0)
        self.qtgui_time_sink_x_0_0_1_1_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0_1_1_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_1_1_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_1_1_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_1_1_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_1_1_0_0.enable_grid(True)
        self.qtgui_time_sink_x_0_0_1_1_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_1_1_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_1_1_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0_1_1_0_0.disable_legend()

        labels = ['Mag', 'real', 'Img', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "dark green", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 3, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0_0_1_1_0_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_0_1_1_0_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_0_1_1_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_1_1_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_1_1_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_1_1_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_1_1_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_1_1_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_1_1_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_1_1_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_1_1_0_0_win)
        self.qtgui_time_sink_x_0_0_1_1_0 = qtgui.time_sink_f(
        	4000000, #size
        	400e3, #samp_rate
        	'Tx Signal', #name
        	3 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_1_1_0.set_update_time(1.0)
        self.qtgui_time_sink_x_0_0_1_1_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0_1_1_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_1_1_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_1_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_1_1_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_1_1_0.enable_grid(True)
        self.qtgui_time_sink_x_0_0_1_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_1_1_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_1_1_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0_1_1_0.disable_legend()

        labels = ['Mag', 'real', 'Img', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "dark green", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 3, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(3):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_1_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_1_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_1_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_1_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_1_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_1_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_1_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_1_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_1_1_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_1_1_0_win)
        self.blocks_complex_to_mag_1 = blocks.complex_to_mag(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.beamforming_matlab_file_payload_py_0 = beamforming.matlab_file_payload_py('/home/gokhan/gnu-radio/gr-beamforming/examples/data/trainingSig1')



        ##################################################
        # Connections
        ##################################################
        self.connect((self.beamforming_matlab_file_payload_py_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.beamforming_matlab_file_payload_py_0, 0), (self.blocks_complex_to_mag_1, 0))
        self.connect((self.beamforming_matlab_file_payload_py_0, 0), (self.qtgui_time_sink_x_0_0_1_1_0_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.qtgui_time_sink_x_0_0_1_1_0, 2))
        self.connect((self.blocks_complex_to_float_0, 0), (self.qtgui_time_sink_x_0_0_1_1_0, 1))
        self.connect((self.blocks_complex_to_mag_1, 0), (self.qtgui_time_sink_x_0_0_1_1_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "trainingSignal_test")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate


def main(top_block_cls=trainingSignal_test, options=None):

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
