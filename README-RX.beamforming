Beamforming Receiver: Execute the below script to run the transmitter on a host PC connected to SDR:

airbeam_test_nogui.py

Important lines to update/edit:

Line #30: self.data_files_path = data_files_path = "/home/genesys/workarea-gnuradio/gnuradio/gr-beamforming/examples/data"

Change the data file path to the proper location where this folder kept in the host PC. Here it is stored at the /home/genesys/workarea-gnuradio/gnuradio location

Line #36: ",".join(("serial=318D28D", "")),

Assign the correct serial number of the usrp radio connected to the host machine running this code execute <uhd_find_devices> in terminal to get the correct serial numbering

Line #42: self.uhd_usrp_source_0.set_clock_source('external', 0)

Make sure the clock source is set to external in order for the SDRs to get 10MHz and PPS reference from Octoclock or RFClock

Line #45: self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(925e6,1e6), 0)

The receive center frequency should match the transmitter frequency. Here it is kept at 925MHz in order to match with the default transmitter frequency. Users can use any frequency of their choosing, within the range of the SDR.

Line #56: self.beamforming_correlate_and_tag_py_0 = beamforming.correlate_and_tag_py(trainingSignal_size, trainingSignal_size + 400 + 256* 64 + 100, 1, data_files_path + "/trainingSig", 1, 0)

Update the number of Transmitters (kept in bold) in the above line. This line calls the correlate_and_tag_py.py script where these inputs are used in line #50: def init(self, seq_len, frame_len, num_Tx, file_path, cor_method, feedback_type)

Line#102 dst_dir = '/home/genesys/KRI_csi_data/flight_pattern'

Update the destination directory for storing the CSI and extracted payload

The corresponding .grc file for the beamforming receiver python script is: examples/airbeam_receiver_test.grc

this file can be opened with gnuradio-companion.

Also, check out my Distributed beamforming Transmitter repository for setting up the transmitter for this beamforming experiment:
https://github.com/Subhramoy/DistributedBeamforming-Transmitter


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
