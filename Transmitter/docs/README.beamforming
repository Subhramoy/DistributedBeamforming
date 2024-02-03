Beamforming Transmitter: 
Execute the below script to run the transmitter on a host PC connected to SDR:
examples/TX2/data_beamforming_tx2_subhro_padding_ID2.py

Important lines to update/edit:

Line #38-39:
        self.tx_id_1 = tx_id_1 = 2
        self.tx_id_0 = tx_id_0 = 1

Setting IDs for transmitter radios. Add more in sequential numbers in the same pattern if you have more than 2 transmitter radios. This code currently supports up to 4 transmitter radios.

Line #54:
        	",".join(("serial=316E275", "")),

Assign the correct serial number of the usrp radio connected to the host machine running this code
execute <uhd_find_devices> in terminal to get the correct serial numbering

Line #60-61:
        self.uhd_usrp_sink_0.set_clock_source('external', 0)
        self.uhd_usrp_sink_0.set_time_source('external', 0)

Make sure the clock and time source are set to external in order for the SDRs to get 10MHz and PPS reference from Octoclock or RFClock

Line #64:
        self.uhd_usrp_sink_0.set_center_freq(uhd.tune_request(925e6, -1e6), 0)

change transmit frequency here. Currently set to 925MHz. Users can use any frequency of their choosing, within the range of the SDR.

Line #101:
        self.beamforming_matlab_file_payload_py_0_0 = beamforming.matlab_file_payload_py('/home/nvidia/workarea-gnuradio/gnuradio/gr-beamforming/examples/data/trainingSig2')

→ Change the directory where you have kept the gr-beamforming folder (Here it is /home/nvidia/workarea-gnuradio/)

→ Change the name of  trainingSig2 to  trainingSig1/trainingSig3/trainingSig4 based on the ID of your transmitter SDR connected to the host PC

Line #109:
	If transmitter ID  = 1, then this should be  tx_id_0
	If transmitter ID  = 2, then this should be  tx_id_1
	If transmitter ID  = 3, then this should be  tx_id_2
	If transmitter ID  = 4, then this should be  tx_id_3

Line #174:
	response = client.request('192.168.1.98')

We use a local NTP server on a ubuntu PC. 
The transmitters and receivers run the NTP client code (line #170-195) for time alignment of the transmitted symbols. 
Here in line #174 the address of the local NTP server is given. Update it with the correct one. 
Also, make sure that the host PCs are properly set up for NTP client-server communication. 
Run <sudo ufw allow 123> in terminal for any firewall issue.

Also, check out my Distributed beamforming Receiver repository for setting up the receiver for this beamforming experiment:
https://github.com/Subhramoy/DistributedBeamforming-Receiver


# Paper
If you use this code in your research, please cite our AirBeam and SABRE papers:

```
@INPROCEEDINGS{9077393,
  author={Mohanti, Subhramoy and Bocanegra, Carlos and Meyer, Jason and Secinti, Gokhan and Diddi, Mithun and Singh, Hanumant and Chowdhury, Kaushik},
  booktitle={2019 IEEE 16th International Conference on Mobile Ad Hoc and Sensor Systems (MASS)}, 
  title={AirBeam: Experimental Demonstration of Distributed Beamforming by a Swarm of UAVs}, 
  year={2019},
  volume={},
  number={},
  pages={162-170},
  keywords={Unmanned Aerial Vehicle;Distributed beamforming;Software Defined Radio;FPGA},
  doi={10.1109/MASS.2019.00028}}
```

```
@ARTICLE{9738441,
  author={Mohanti, Subhramoy and Bocanegra, Carlos and Sanchez, Sara Garcia and Alemdar, Kubra and Chowdhury, Kaushik Roy},
  journal={IEEE Transactions on Wireless Communications}, 
  title={SABRE: Swarm-Based Aerial Beamforming Radios: Experimentation and Emulation}, 
  year={2022},
  volume={21},
  number={9},
  pages={7460-7475},
  keywords={Array signal processing;Receivers;Autonomous aerial vehicles;Synchronization;Channel estimation;Signal to noise ratio;Radio transmitters;Unamanned aerial vehicle;distributed aerial beamforming;coordinated beamforming;resource allocation;IEEE 80211be;WiFi 7;5G;multi-transmitter coordination},
  doi={10.1109/TWC.2022.3158866}}
```
