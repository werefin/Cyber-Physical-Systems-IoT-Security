#!/usr/bin/env python3

import socket
import json
import struct
import time

TCP_IP = '169.254.26.44'
TCP_PORT = 5020
BUFFER_SIZE = 1024

# Incremental
TRANSACTION_IDENTIFIER = 1

# These values are always the same
PROTOCOL_ID = b'\x00\x00'
LENGTH = b'\x00\x06'
UNIT_ID = b'\x00'

# Base part of the modbus message
base_prot = PROTOCOL_ID + LENGTH + UNIT_ID

options = {

'ACTIONS': {
'READ_COIL': b'\x01',
'WRITE_COIL': b'\x05'
},

'ADDRESS': {
'1': b'\x00\x01',
'2': b'\x00\x02',
'3': b'\x00\x03'
},

'VALUE': {
'TRUE': b'\xff\x00',
'FALSE': b'\x00\x00',
'READ': b'\x00\x01'
}

}

def trans_id_to_bytes(trans_id):
	trans_id = trans_id.to_bytes(2, 'big')
	return trans_id

def write_coil(trans_id, address, value):
	message = trans_id_to_bytes(trans_id) + base_prot + options['ACTIONS']['WRITE_COIL'] + options['ADDRESS'][address] + options['VALUE'][value]
	return message

def read_coil(trans_id, address, value):
	message = trans_id_to_bytes(trans_id) + base_prot + options['ACTIONS']['READ_COIL'] + options['ADDRESS'][address] + options['VALUE'][value]
	return message

# Start connection to client
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

# Start sending packets
while True:
	message = write_coil(TRANSACTION_IDENTIFIER, '1', 'FALSE')
	TRANSACTION_IDENTIFIER += (1 % 255)
	s.send(message)
	time.sleep(0.001)
	message = write_coil(TRANSACTION_IDENTIFIER, '2', 'FALSE')
	TRANSACTION_IDENTIFIER += (1 % 255)
	s.send(message)
	time.sleep(0.001)

s.close()