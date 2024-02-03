#!/usr/bin/python

import json
import matplotlib.pyplot as plt
import numpy as np
import scipy.io

np.count = [0]* 1000

np.check_time = [0]* 1000
	
with open('GPSDO_Lock_Data_KRI_80135.txt') as json_data:
	de_serialized = json.load(json_data)

for iteration in range (1000):
	target_object = de_serialized[iteration]
	if target_object['GPS_Lock'] == 1:
		np.check_time[iteration] = target_object['GPS_Lock_Check_Time']
		np.count[iteration] = 1
	if iteration == 0:
		start_time = target_object['GPS_Lock_Check_Time']
	if iteration == 999:
		stop_time = target_object['GPS_Lock_Check_Time']

elapsed_time_80135 = stop_time - start_time

scipy.io.savemat('GPSDO_Lock_Data_KRI_80135.mat', dict(time_80135KRI=np.check_time, lock_80135KRI=np.count))


'''np.count = [0]* 1000

np.check_time = [0]* 1000
	
with open('GPSDO_Lock_Data_80122.txt') as json_data:
	de_serialized = json.load(json_data)

for iteration in range (1000):
	target_object = de_serialized[iteration]
	if target_object['GPS_Lock'] == 1:
		np.check_time[iteration] = target_object['GPS_Lock_Check_Time']
		np.count[iteration] = 1
	if iteration == 0:
		start_time = target_object['GPS_Lock_Check_Time']
	if iteration == 999:
		stop_time = target_object['GPS_Lock_Check_Time']

elapsed_time_802122 = stop_time - start_time

scipy.io.savemat('GPSDO_Lock_Data_Indoor_SIm_80122.mat', dict(time_80122=np.check_time, lock_80122=np.count))'''
