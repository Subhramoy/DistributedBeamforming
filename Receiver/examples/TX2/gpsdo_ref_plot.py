#!/usr/bin/python

import json
import matplotlib.pyplot as plt
import numpy as np
import scipy.io


np.count = [0]* 100000

np.check_time = [0]* 100000
	
with open('GPSDO_Lock_Data_80111.txt') as json_data:
	de_serialized = json.load(json_data)

for iteration in range (100000):
	target_object = de_serialized[iteration]
	if target_object['Reference_Lock'] == 1:
		np.check_time[iteration] = target_object['Ref_Lock_Check_Time']
		np.count[iteration] = 1
	if iteration == 0:
		start_time = target_object['Ref_Lock_Check_Time']
	if iteration == 99999:
		stop_time = target_object['Ref_Lock_Check_Time']

elapsed_time_802111 = stop_time - start_time

scipy.io.savemat('GPSDO_RefLock_Data_80111.mat', dict(time_ref_80111=np.check_time, ref_lock_80111=np.count))


np.count = [0]* 100000

np.check_time = [0]* 100000
	
with open('GPSDO_Lock_Data_80122.txt') as json_data:
	de_serialized = json.load(json_data)

for iteration in range (100000):
	target_object = de_serialized[iteration]
	if target_object['Reference_Lock'] == 1:
		np.check_time[iteration] = target_object['Ref_Lock_Check_Time']
		np.count[iteration] = 1
	if iteration == 0:
		start_time = target_object['Ref_Lock_Check_Time']
	if iteration == 99999:
		stop_time = target_object['Ref_Lock_Check_Time']

elapsed_time_802122 = stop_time - start_time

scipy.io.savemat('GPSDO_RefLock_Data_80122.mat', dict(time_ref_80122=np.check_time, ref_lock_80122=np.count))
