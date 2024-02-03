% clc;close all;clear all;
%load ('GPSDO_RefLock_Data_80111.mat');
load ('GPSDO_Lock_Data_ColmbsAveParking_80122.mat');
figure();
hold on;
%plot (ref_lock_80111)
plot (lock_80135)
ylim([0 1.2])
xticklabels('%3.9f',time_80135)

