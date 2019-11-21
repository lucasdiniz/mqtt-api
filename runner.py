#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
Publish some messages to queue
"""
import paho.mqtt.publish as publish
import paho.mqtt.client as paho
from datetime import datetime
from mqtt_publisher import MqttPublisher
from http_poster import HttpPoster

MQTT_HOST = "test.mosquitto.org"
MQTT_PORT=1883
MQTT_TRANSPORT="tcp"
SMALL_DATA_FILE="data/small_data.json"
MEDIUM_DATA_FILE="data/medium_data.json"
BIG_DATA_FILE="data/big_data.json"

HTTP_SERVER="http://jsonplaceholder.typicode.com/posts"


if __name__ == '__main__':
	with open(SMALL_DATA_FILE, 'r') as file:
		for iteration in range(1, 30):
			# POST TO HTTP SERVER
			data_to_be_published = file.read()
			httpPoster = HttpPoster(HTTP_SERVER, data_to_be_published, SMALL_DATA_FILE, iteration)
			httpPoster.post()
			# PUBLISH TO MQTT BROKER
			pubInstance = MqttPublisher(data_to_be_published, MQTT_HOST, MQTT_PORT, MQTT_TRANSPORT, SMALL_DATA_FILE, iteration)
			pubInstance.publish_messages()
	with open(MEDIUM_DATA_FILE, 'r') as file:
		for iteration in range(1, 30):
			# POST TO HTTP SERVER
			data_to_be_published = file.read()
			httpPoster = HttpPoster(HTTP_SERVER, data_to_be_published, MEDIUM_DATA_FILE, iteration)
			httpPoster.post()
			# PUBLISH TO MQTT BROKER
			pubInstance = MqttPublisher(data_to_be_published, MQTT_HOST, MQTT_PORT, MQTT_TRANSPORT, MEDIUM_DATA_FILE, iteration)
			pubInstance.publish_messages()
	with open(BIG_DATA_FILE, 'r') as file:
		for iteration in range(1, 30):
			# POST TO HTTP SERVER
			data_to_be_published = file.read()
			httpPoster = HttpPoster(HTTP_SERVER, data_to_be_published, BIG_DATA_FILE, iteration)
			httpPoster.post()
			# PUBLISH TO MQTT BROKER
			pubInstance = MqttPublisher(data_to_be_published, MQTT_HOST, MQTT_PORT, MQTT_TRANSPORT, BIG_DATA_FILE, iteration)
			pubInstance.publish_messages()