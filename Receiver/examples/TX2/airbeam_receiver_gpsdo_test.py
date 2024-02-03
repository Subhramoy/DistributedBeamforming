#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Airbeam Test
# Generated: Fri Mar 22 15:47:59 2019
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
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import beamforming
import sip
import sys
import time
from gnuradio import qtgui
import cons_config  # embedded python module
import pmt
import wx
import os, threading
import ntplib
import subprocess


class airbeam_test(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Airbeam Test")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Airbeam Test")
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

        self.settings = Qt.QSettings("GNU Radio", "airbeam_test")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.trainingSignal_size = trainingSignal_size = 16456
        self.samp_rate = samp_rate = 400e3
        self.data_files_path = data_files_path = "/home/genesys/workarea-gnuradio/gnuradio/gr-beamforming/examples/data"

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("serial=30BC5F6", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_clock_source('gpsdo', 0)
        self.uhd_usrp_source_0.set_time_source('gpsdo', 0)
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_time_unknown_pps(uhd.time_spec())
        self.uhd_usrp_source_0.set_center_freq(900e6, 0)
        self.uhd_usrp_source_0.set_gain(40, 0)
        self.uhd_usrp_source_0.set_antenna('RX2', 0)
        self.uhd_usrp_source_0.set_bandwidth(400e3, 0)
        self.qtgui_time_sink_x_0_0_1_1_0_0_0 = qtgui.time_sink_f(
        	200000, #size
        	samp_rate, #samp_rate
        	'XCor', #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_1_1_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_1_1_0_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0_1_1_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_1_1_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_1_1_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_1_1_0_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0_1_1_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_1_1_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_1_1_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_1_1_0_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0_1_1_0_0_0.disable_legend()

        labels = ['IQ', 'Corr Output', '', '', '',
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

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_1_1_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_1_1_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_1_1_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_1_1_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_1_1_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_1_1_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_1_1_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_1_1_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_1_1_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_1_1_0_0_0_win)
        self.qtgui_time_sink_x_0_0_1_1_0_0 = qtgui.time_sink_c(
        	200000, #size
        	samp_rate, #samp_rate
        	'Tx Signal', #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_1_1_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_1_1_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0_1_1_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_1_1_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_1_1_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_1_1_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0_1_1_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_1_1_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_1_1_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_1_1_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0_1_1_0_0.disable_legend()

        labels = ['IQ', 'Corr Output', '', '', '',
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
        self.qtgui_freq_sink_x_0_0_0_0 = qtgui.freq_sink_c(
        	256*8, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	900e6, #fc
        	samp_rate, #bw
        	'Tx Signal', #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_0_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0_0_0.set_plot_pos_half(not True)

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
                self.qtgui_freq_sink_x_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_0_0_win)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, '/tmp/payload.dat', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.beamforming_filter_payload_py_0 = beamforming.filter_payload_py('payload')
        self.beamforming_correlate_and_tag_py_0 = beamforming.correlate_and_tag_py(trainingSignal_size, trainingSignal_size + 400 + 256* 64 + 100, 2, data_files_path + "/trainingSig", 1, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.beamforming_correlate_and_tag_py_0, 0), (self.beamforming_filter_payload_py_0, 0))
        self.connect((self.beamforming_correlate_and_tag_py_0, 1), (self.blocks_complex_to_mag_0, 0))
        self.connect((self.beamforming_correlate_and_tag_py_0, 0), (self.qtgui_freq_sink_x_0_0_0_0, 0))
        self.connect((self.beamforming_correlate_and_tag_py_0, 0), (self.qtgui_time_sink_x_0_0_1_1_0_0, 0))
        self.connect((self.beamforming_filter_payload_py_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_complex_to_mag_0, 0), (self.qtgui_time_sink_x_0_0_1_1_0_0_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.beamforming_correlate_and_tag_py_0, 0))


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
	###############################
	# GPS lock and 10MHz REF lock##
	###############################
	#check for gps lock
	gps_lock=self.uhd_usrp_source_0.get_mboard_sensor("gps_locked",0)
	#check for ref lock
	ref_lock=self.uhd_usrp_source_0.get_mboard_sensor("ref_locked",0)
	if ref_lock.to_bool() == False:
		print "!!!!!No Ref Lock!!!!!"
		#for in range (300):
		#	ref_lock=self.uhd_usrp_source_0.get_mboard_sensor("ref_locked",0)
		#if ref_lock.to_bool() == False:
		#	print "!!!!!No Ref Lock!!!!!"
			
	if gps_lock.to_bool() == False:
       		print "!!!!!No GPS sync!!!!!"
	else:
		#initialization of USRP's internal clock to gps_time
        	#find moment of impulse on pps line
		last_pps_time = self.uhd_usrp_source_0.get_time_last_pps()
		a=0
		b=0
        	while last_pps_time.get_real_secs() == self.uhd_usrp_source_0.get_time_last_pps().get_real_secs():
			#time.sleep(0.1)
			#print "USRP PPS time syncing ..."
			a=a+1
		print a		
		#get current gps_time
		gps_time=self.uhd_usrp_source_0.get_mboard_sensor("gps_time",0)
		#set the gps_time+1 on the next pps edge
		self.uhd_usrp_source_0.set_time_next_pps(uhd.time_spec(gps_time.to_int()+1))
		last_pps_time = self.uhd_usrp_source_0.get_time_last_pps()
  		#wait for change to take effect
             	while last_pps_time.get_real_secs() == self.uhd_usrp_source_0.get_time_last_pps().get_real_secs():
			#time.sleep(0.1)
			#print "USRP time syncing ..."
			b=b+1
		print b	
	##self.uhd_usrp_sink_0.set_time_unknown_pps(uhd.time_spec_t(system_time +1))	
	#self.uhd_usrp_source_0.set_time_next_pps(uhd.time_spec_t(system_time +1))
		self.uhd_usrp_source_0.set_start_time(uhd.time_spec_t(gps_time.to_int() + wait_time))
		print "wait over"
		print "Tranmission will start after {} seconds".format(wait_time)
	lock.release()
	time.sleep(wait_time-2)

	##################################################
	# Other functions
	##################################################

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "airbeam_test")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_trainingSignal_size(self):
        return self.trainingSignal_size

    def set_trainingSignal_size(self, trainingSignal_size):
        self.trainingSignal_size = trainingSignal_size

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0_1_1_0_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0_1_1_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0_0_0_0.set_frequency_range(900e6, self.samp_rate)

    def get_data_files_path(self):
        return self.data_files_path

    def set_data_files_path(self, data_files_path):
        self.data_files_path = data_files_path


def main(top_block_cls=airbeam_test, options=None):

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
