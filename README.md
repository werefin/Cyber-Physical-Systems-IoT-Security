# Cyber-Physical Systems & IoT Security - Labs

This repository contains some of the most interesting labs for CPS & IoT security course.

## ICS - Anomaly Detection

In this case, we use an autoencoder for anomaly detection. The intuition is the following: if we train
our autoencoder on normal data ([HAI](https://github.com/icsdataset/hai)), the reconstruction error on malicious data would be
higher with respect to normal data. Therefore, in the code, we will train our
autoencoder in one of the training datasets, which is composed of only benign
samples. Then, we extract the standard deviation of the loss as a threshold to
discriminate between attacks and normal samples. Since we will use only benign data
during training, this process is usually called One Class Classification. No big optimization
has been done in the code.

## Modbus Hacking

In the hacked network there is a Modbus server controlling two LEDs, the states of the LEDs are
ON and OFF. In the same network there is a Modbus client managing the state of the LEDs, sending
Modbus messages through TCP/IP. In addition, the server can handle multiple connection at the same
time. The goal is to get the modbus packets, understand the protocol structure and inject messages in order to
control the LEDs. In a second time, it's possible to DoS the server in order to keep the LEDs off.
