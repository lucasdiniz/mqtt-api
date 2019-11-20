#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
Publish some messages to queue
"""
import paho.mqtt.publish as publish
import paho.mqtt.client as paho
from datetime import datetime
from mqtt_publisher import MqttPublisher

HOST = "test.mosquitto.org"
PORT=1883
TRANSPORT="tcp"
SMALL_DATA_FILE="data/small_data.json"
MEDIUM_DATA_FILE="data/medium_data.json"
BIG_DATA_FILE="data/big_data.json"

if __name__ == '__main__':
	with open(SMALL_DATA_FILE, 'r') as file:
		for iteration in range(1, 30):
			data_to_be_published = file.read()
			pubInstance = MqttPublisher(data_to_be_published, HOST, PORT, TRANSPORT, SMALL_DATA_FILE, iteration)
			pubInstance.publish_messages()
	with open(MEDIUM_DATA_FILE, 'r') as file:
		for iteration in range(1, 30):
			data_to_be_published = file.read()
			pubInstance = MqttPublisher(data_to_be_published, HOST, PORT, TRANSPORT, MEDIUM_DATA_FILE, iteration)
			pubInstance.publish_messages()
	with open(BIG_DATA_FILE, 'r') as file:
		for iteration in range(1, 30):
			data_to_be_published = file.read()
			pubInstance = MqttPublisher(data_to_be_published, HOST, PORT, TRANSPORT, BIG_DATA_FILE, iteration)
			pubInstance.publish_messages()