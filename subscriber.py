#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A small example subscriber
"""
import paho.mqtt.client as paho
import paho.mqtt.subscribe as subscribe

host = "test.mosquitto.org"
PORT=1883
TRANSPORT="tcp"

def on_message(mosq, obj, msg):
    print "%-20s %d %s" % (msg.topic, msg.qos, msg.payload)
    mosq.publish('pong', 'ack', 0)

def on_publish(mosq, obj, mid):
    pass

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

if __name__ == '__main__':
    client = paho.Client(transport=TRANSPORT)
    client.on_message = on_message
    client.on_publish = on_publish
    client.on_connect = on_connect

    #client.tls_set('root.ca', certfile='c1.crt', keyfile='c1.key')
    client.connect(host, PORT, 60)

    client.subscribe("kids/yolo", 0)
    client.subscribe("adult/#", 0)

    while client.loop() == 0:
        pass

# vi: set fileencoding=utf-8 :