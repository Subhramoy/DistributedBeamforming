#!/usr/bin/python
## @note This file is NOT in use.
# Test script to compare it with equivalent MATLAB function.
import numpy


# Test inputs

channel_est = [  0.4972 - 0.5409j,  -0.0038 - 0.4609j,  -0.0767 + 0.7706j,  -0.1477 + 0.6706j]
channel_est = numpy.multiply (channel_est , 1.0e-03)


channel_est = [0.9955639+0.j, 0.+0.j]

print "Before WF beamweigts: {}".format(channel_est)

def pow2db(a):
    return 10*numpy.log10(a)

# def calculate_weights(channel_estimations):
## Static variables
DeltaP = 0
inc = 0.001
SINRdb = 20
Atx = 0
Gtx = 0
Noise = 105
BBPowMax = 6327e+03
BBPowPayload = 9.1553e-05


chEst_abs = numpy.absolute(channel_est)  # Channel gain
w_abs = numpy.zeros(len(channel_est), dtype=float)  # Inizialization of weight power
Niter = 1;  # initialize number of total iterations

## Check if requested SNR is attainable
# P_ch = -pow2db(chEst*chEst');
P_ch = -1*pow2db( # pow2db
                    numpy.matmul( # Matrix multiply
                        channel_est, # CE array
                        numpy.matrix(channel_est).getH() # Complex conjugate
                        )
                    )

P_ch = P_ch.item(0,0)


#BBPowMax_rep = repmat(BBPowPayload*BBPowMax,1,length(channel_estimations));
BBPowMax_rep = numpy.repeat(BBPowPayload*BBPowMax,len(channel_est));

#P_tx_offered = pow2db(sum(BBPowMax_rep)) + 30;
P_tx_offered = pow2db(numpy.sum(BBPowMax_rep)) + 30;

#SNRdb_offered = P_tx_offered + Atx + Gtx - P_ch + Noise;
SNRdb_offered = P_tx_offered + Atx + Gtx - P_ch + Noise;

if SNRdb_offered < SINRdb:
    print('WARNING - Cannot achieve SNR. {}}vs {}} (dB)'.format(SNRdb_offered,SINRdb))
    print('WARNING - Consider revising Gains\n');
    w_abs = numpy.sqrt(BBPowMax)  # assign maximum

else:
    # Water filling - power allocation
    targetBB = SINRdb + P_ch - Atx - Gtx - Noise - 30  # in dB (not in dBm, important)
    print targetBB
    # print numpy.real(targetBB)

    #while pow2db(BBPowPayload*(w_abs*w_abs')) < targetBB
while (pow2db( BBPowPayload * numpy.matmul(
                                        w_abs,
                                        numpy.matrix(w_abs).getH()
                                        ).item(0,0) )
                                    ) < numpy.real(targetBB):

    # [~,idxvalids] = find(w_abs.^2 + inc < BBPowMax);
    #print BBPowMax
    #print numpy.power(w_abs, 2) + inc
    idxvalids = numpy.nonzero(numpy.power(w_abs, 2) + inc < BBPowMax)[0]
    #print idxvalids
    if idxvalids.size == 0:
        break

    # Locate the lowest noise level channel
    index = numpy.argsort(numpy.power(w_abs[idxvalids], 2) + numpy.power(numpy.divide(1, chEst_abs[idxvalids]),2 ))

    # Otherwise go to the next smallest power channel

    w_abs[idxvalids[index[0]]] = w_abs[idxvalids[index[0]]] + inc
    #print('iter {}- Achieved Power = {} (dBm)\n'.format(Niter,pow2db(w_abs*ww_abs')))
    Niter = Niter + 1
    #print          w_abs
    # print  numpy.absolute(targetBB)

# Assign weights (phase and power)
beamWeight_angle = numpy.transpose( numpy.multiply(-1, numpy.angle(channel_est)) )         # Phase equalization
beamWeights =   numpy.multiply(w_abs, numpy.add(
                            numpy.cos(beamWeight_angle),
                            numpy.multiply(0+1j, numpy.sin(beamWeight_angle))
                            ))

print "WF algorith took: {} iterations".format(Niter)
print "After WF beamweigts: {}".format(beamWeights)



#    return BBPowPayload


"""
if __name__ == '__main__':
    print calculate_weights(channel_est)
"""
