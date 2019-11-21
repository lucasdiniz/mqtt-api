#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
a publisher class
"""

import paho.mqtt.publish as publish
import paho.mqtt.client as paho
from datetime import datetime
import time
import csv
import os

class MqttPublisher:
	PROTOCOL="MQTT"
	PUBLISH_TIME=None
	ACK_TIME=None
	client=None
	RESULTS_FILE="results/results.csv"
	def __init__(self, message, host, port, transport, file_name, iteration):
		# The message that shall be published
		self.message = message
		self.host = host
		self.port = port
		self.transport = transport
		self.file_name = file_name
		self.iteration = iteration
		print("Publish iteration number %d starting..." % (self.iteration))
		self.connect()

	# Callback called when publish ACK is received from broker
	def on_publish(self, client,userdata,result):
		self.ACK_TIME = datetime.now()
		print("Received Publish ACK from broker: %s" % (self.ACK_TIME))

	def connect(self):
		self.client= paho.Client(transport=self.transport)
		self.client.on_publish = self.on_publish
		self.client.loop_start()
		self.client.connect(host=self.host,port=self.port) 
		return self.client

	def publish_messages(self):
		# publish a single message
		self.PUBLISH_TIME = datetime.now()
		print("Publishing data to broker: %s" % (self.PUBLISH_TIME))
		ret = self.client.publish(topic="kids/yolo", payload=self.message, qos=1)
		ret.wait_for_publish()
		self.client.loop_stop()
		duration = self.ACK_TIME - self.PUBLISH_TIME
		duration_micro=duration.microseconds
		print("Elapsed time: %s microseconds" % (duration_micro))
		self.write_results(os.stat(self.file_name).st_size, duration_micro, self.file_name, self.iteration)
		self.client.disconnect()

	def write_results(self, file_size, duration_micro, size_name, iteration):
		print("Writing results for publishing %s to %s\n" % (self.file_name, self.RESULTS_FILE))
		with open(self.RESULTS_FILE, 'a') as csvFile:
			writer = csv.writer(csvFile)
			writer.writerow([self.PROTOCOL, file_size, duration_micro, size_name, iteration])
		csvFile.close()
