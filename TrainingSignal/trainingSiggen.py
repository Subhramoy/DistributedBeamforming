#!/usr/bin/python


from __future__ import division
import struct
import sys
import numpy
import math
import cmath

trainingSig1 = []
trainingSig2 = []
trainingSig3 = []
trainingSig4 = []


##Real part of the training signal for antenna #1 read from file
with open('trainingSig1_real.txt', 'r') as f:
    pay_real = [line.strip() for line in f]

length = (len(pay_real))

##Imaginary part of the training signal for antenna #1 read from file
with open('trainingSig1_imag.txt', 'r') as f1:
    pay_imag = [line.strip() for line in f1]

##Reconstructing the training signal for antenna #1 in complex format
for ii in range (length):
    pay_c = complex (float(pay_real[ii]), float(pay_imag[ii]))
    trainingSig1.append(pay_c)
################################################################################

##Real part of the training signal for antenna #2 read from file
with open('trainingSig2_real.txt', 'r') as f:
    pay_real = [line.strip() for line in f]

length = (len(pay_real))

##Imaginary part of the training signal for antenna #2 read from file
with open('trainingSig2_imag.txt', 'r') as f1:
    pay_imag = [line.strip() for line in f1]

##Reconstructing the training signal for antenna #2 in complex format
for ii in range (length):
    pay_c = complex (float(pay_real[ii]), float(pay_imag[ii]))
    trainingSig2.append(pay_c)
################################################################################

##Real part of the training signal for antenna #3 read from file
with open('trainingSig3_real.txt', 'r') as f:
    pay_real = [line.strip() for line in f]

length = (len(pay_real))

##Imaginary part of the training signal for antenna #3 read from file
with open('trainingSig3_imag.txt', 'r') as f1:
    pay_imag = [line.strip() for line in f1]

##Reconstructing the training signal for antenna #3 in complex format
for ii in range (length):
    pay_c = complex (float(pay_real[ii]), float(pay_imag[ii]))
    trainingSig3.append(pay_c)
################################################################################

##Real part of the training signal for antenna #4 read from file
with open('trainingSig4_real.txt', 'r') as f:
    pay_real = [line.strip() for line in f]

length = (len(pay_real))

##Imaginary part of the training signal for antenna #4 read from file
with open('trainingSig4_imag.txt', 'r') as f1:
    pay_imag = [line.strip() for line in f1]

##Reconstructing the training signal for antenna #4 in complex format
for ii in range (length):
    pay_c = complex (float(pay_real[ii]), float(pay_imag[ii]))
    trainingSig4.append(pay_c)
################################################################################

#with open('symbolmatrix.txt', 'w') as f12:
#    for item in symbol64qam:0
#        f12.write("%s\t" % item)
