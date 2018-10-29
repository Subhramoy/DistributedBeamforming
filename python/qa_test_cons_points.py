import os, sys
sys.path.append(os.path.abspath("/home/gokhan/gnu-radio/gr-beamforming/examples"))
import cons_config as cc


print ("64QAM")
print len(cc.get_points("64QAM"))
print cc.get_points("64QAM")


print ("32QAM")
print len(cc.get_points("32QAM"))
print cc.get_points("32QAM")


print ("16QAM")
print len(cc.get_points("16QAM"))
print cc.get_points("16QAM")



print ("8QAM")
print len(cc.get_points("8QAM"))
print cc.get_points("8QAM")

print ("QPSK")
print len(cc.get_points("QPSK"))
print cc.get_points("QPSK")


print ("BPSK")
print len(cc.get_points("BPSK"))
print cc.get_points("BPSK")