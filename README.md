# Cyber-Physical Systems & IoT Security - Labs

This repository contains some of the most interesting labs for CPS & IoT security course.

## ICS - Anomaly Detection

In this case, we use an autoencoder for anomaly detection. The intuition is the following: if we train our autoencoder on normal data ([HAI](https://github.com/icsdataset/hai)), the reconstruction error on malicious data would be higher with respect to normal data. Therefore, in the code, we will train our autoencoder in one of the training datasets, which is composed of only benign samples. Then, we extract the standard deviation of the loss as a threshold to discriminate between attacks and normal samples. Since we will use only benign data during training, this process is usually called One Class Classification. No huge optimization has been done in the code.

## Modbus Hacking

The purpose of the conducted investigation is to assess the network under examination, wherein a Modbus server is responsible for controlling two LEDs, toggling their states between ON and OFF. Concurrently, a Modbus client is present within the same network, tasked with managing the LED states by transmitting Modbus messages over TCP/IP. It should be emphasized that the disclosed code is intended solely for research purposes, specifically for examining the network's vulnerability to Denial of Service (DoS) attacks. The primary objective of this investigation is to comprehend the underlying protocol structure of the Modbus packets and subsequently employ message injection techniques to manipulate the states of the LEDs, granting control over their functionality. Furthermore, a secondary aim is to assess the server's susceptibility to a DoS attack, effectively disrupting its normal operations and causing the LEDs to remain in the OFF state for an extended duration. In this repository, we report two types of possible attacks, with corresponding code implementations, based on the aforementioned scenario.

**Note**: all activities conducted herein are solely intended for academic and research purposes and should not be utilized in any way that would violate ethical or legal standards. The findings of this investigation aim to contribute to the enhancement of network security and the development of robust countermeasures against potential vulnerabilities.
