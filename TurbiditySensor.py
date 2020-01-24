#!/usr/bin/env python
import cayenne.client
import time
import logging
import smbus

# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "3baa9320-3aa9-11ea-a38a-d57172a4b4d4"
MQTT_PASSWORD  = "95a5bce532fa419bb8d44db8a048bf8df676c1df"
MQTT_CLIENT_ID = "160c3b90-3dca-11ea-a38a-d57172a4b4d4"
address = 0x48
A0 = 0x40
bus = smbus.SMBus(1)


# The callback for when a message is received from Cayenne.
def on_message(message):
    print("message received: " + str(message))
    # If there is an error processing the message return an error string, otherwise return nothing.
    
client = cayenne.client.CayenneMQTTClient()
client.on_message = on_message
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, loglevel=logging.INFO)
# For a secure connection use port 8883 when calling client.begin:
# client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, port=8883, loglevel=logging.INFO)

i=0
timestamp = 0

while True:
    client.loop()
    if (time.time() > timestamp + 10):
        bus.write_byte(address,A0)
        value = bus.read_byte(address)
        client.virtualWrite(1, value)
        timestamp = time.time()
        i = i+1
