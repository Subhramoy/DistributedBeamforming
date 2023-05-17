#!/usr/bin/python


from __future__ import division
import struct
import sys
import numpy
import math
import cmath


numTxAntennas = 1
binary_byte_read = 8
channel_est_antennas = []
beamweights =[]
payload = []
pay_c = []
bmwght_temp = []
bmfrm_pyld = []
beamform_payload = []

##Real part of the payload read from 'payload_real.txt' file
with open('payload_real.txt', 'r') as f:
    pay_real = [line.strip() for line in f]

length = (len(pay_real))

##Imaginary part of the payload read from 'payload_imag.txt' file
with open('payload_imag.txt', 'r') as f1:
    pay_imag = [line.strip() for line in f1]

##Reconstructing the payload in complex format
for ii in range (length):
    pay_c = complex (float(pay_real[ii]), float(pay_imag[ii]))
    payload.append(pay_c)

##Extracting the real and imaginary values of channel estimation
##First 8 bytes of binary file 'weights_tx2.bin' contain real values
##Second 8 bytes of binary file 'weights_tx2.bin' contain imaginary values
##Thrd 8 bytes of binary file 'weights_tx2.bin' contain the time correction value.
sbet_file = open('weights_tx2.bin')
sbet_data = sbet_file.read()
real = struct.unpack('d',sbet_data[0:binary_byte_read])[0]
print(real)
imaginary = struct.unpack('d',sbet_data[binary_byte_read:2*binary_byte_read])[0]
print(imaginary)
time_correct = struct.unpack('d',sbet_data[2*binary_byte_read:3*binary_byte_read])[0]
print(time_correct)

##Recontructing channel estimation value in complex format
channel_est = [real, imaginary]
channel_est_complex = complex(real, imaginary)

##Since I have only 1 Tx radio now, I'm assuming channel estimation values for each antenna to be same
for i in range (numTxAntennas):
    channel_est_antennas.append(channel_est_complex)

##Creating absolute value of channel estimation and then performing phase correction
abs_channel_est_antennas = map(abs, channel_est_antennas)
phase_correction = [x/y for x, y in zip(channel_est_antennas, abs_channel_est_antennas)]

##Create a list of ones corresponding to number of tx antennas. They do it matlab, not sure why
for i in range (numTxAntennas):
    beamweights.append(1)

##Calculating the beamweights
new_beamweights = [a/b for a, b in zip(beamweights, phase_correction)]

##Creating a list (of same length as of payload) of the same beamweight, for multiplication in next step
for xx in range (length):
    bmwght_temp.extend(new_beamweights)

##Payload multiplied with beamweight. 'beamform_payload' will be the output
for xx in range (length):
    bmfrm_pyld = payload[xx]*bmwght_temp[xx]
    beamform_payload.append(bmfrm_pyld)
