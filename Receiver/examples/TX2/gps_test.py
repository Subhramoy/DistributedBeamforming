#!/usr/bin/python

from gnuradio import uhd
#import cons_config  # embedded python module
import pmt
import time
import sys
import wx
import os, threading
import ntplib
import subprocess
import json


###############################
# GPS lock and 10MHz REF lock##
###############################

uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("serial=316E293", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
)
uhd_usrp_sink_0.set_clock_source('gpsdo', 0)
uhd_usrp_sink_0.set_time_source('gpsdo', 0)

count = 0
dict_objects = []
gpsii=0
lock = threading.Lock()
lock.acquire()

#client = ntplib.NTPClient()
#response = client.request('10.42.0.1')
#response = client.request('pool.ntp.org')
#os.system('date ' + time.strftime('%m%d%H%M%Y.%S',time.localtime(response.tx_time)))

#os.system(time.strftime('%m%d%H%M%Y.%S',time.localtime(response.tx_time)))
#system_time_min = int(time.strftime('%M'))
#system_time_min = (system_time_min*60)
        
#print (system_time_min)
#system_time_sec = int(time.strftime('%S'))
#print (system_time_sec)
#system_time_str = (system_time_min + system_time_sec)
#wait_time = 60 - system_time_sec
#print "Tranmission will start after {} seconds".format(wait_time)
#print(system_time_str) 
#system_time = int(system_time_str)
#self.uhd_usrp_sink_0.set_time_unknown_pps(uhd.time_spec_t(system_time +1))	
#uhd_usrp_sink_0.set_time_next_pps(uhd.time_spec_t(system_time +1))

while count<1000:
	start = time.time()
	#check for gps lock
	gps_lock=uhd_usrp_sink_0.get_mboard_sensor("gps_locked",0)
	#check for ref lock
	ref_lock=uhd_usrp_sink_0.get_mboard_sensor("ref_locked",0)

	if ref_lock.to_bool() == False:
		print "!!!!!No Ref Lock!!!!!"
		ref_lock = 0
		ref_lock_time=time.time()
	else:
		#print "Reference Locked"
		ref_lock = 1
		ref_lock_time=time.time()
		
	if gps_lock.to_bool() == False:
		#print "!!!!!No GPS sync!!!!!"
		gps_lock = 0
		gps_time=uhd_usrp_sink_0.get_mboard_sensor("gps_time",0)
		gps_seconds = gps_time.to_int()
		last_pps_time = uhd_usrp_sink_0.get_time_last_pps().to_ticks(1.0)
		gps_lock_time = time.time()
	elif gps_lock.to_bool() == True:
		#print "GPS Locked"
		gps_lock = 1
		gpsii=gpsii+1
		gps_lock_time = time.time()
		#initialization of USRP's internal clock to gps_time

		#get current gps_time
		gps_time=uhd_usrp_sink_0.get_mboard_sensor("gps_time",0)
		gps_seconds = gps_time.to_int()
		#set the gps_time+1 on the next pps edge
		if count == 1:
			uhd_usrp_sink_0.set_time_next_pps(uhd.time_spec(gps_time.to_int()+1))
       		#find moment of impulse on pps line	
		last_pps_time = uhd_usrp_sink_0.get_time_last_pps().to_ticks(1.0)
		print count
		print "GPS Seconds"
		print gps_seconds
		print "PPS Seconds"
		print last_pps_time
	stop = time.time()
	duration = stop - start
	#print duration
        dict_objects.append(
		{
			"Iteration": count,
                        "Reference_Lock": ref_lock,
                        "GPS_Lock": gps_lock,
                        "GPS_Seconds": gps_seconds,
			"Last_PPS_Time": last_pps_time,
			"Ref_Lock_Check_Time": ref_lock_time,
			"GPS_Lock_Check_Time": gps_lock_time
		}
	)
	count = count + 1
	#time.sleep(0.02)


lock.release()
serialized = json.dumps(dict_objects, indent=4)
#print serialized
print gpsii
f = open("GPSDO_Lock_Data_KRI_80135.txt", "w")
f.write(serialized)
f.close()
