import time
import json
import paho.mqtt.client as paho
from paho import mqtt
# read from .env
import os
from dotenv import load_dotenv
load_dotenv()



# setting callbacks for different events to see if it works, print the message etc.
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

# with this callback you can see if your publish was successful
def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))

# using MQTT version 5 here, for 3.1.1: MQTTv311, 3.1: MQTTv31
# userdata is user defined data of any type, updated by user_data_set()
# client_id is the given name of the client
client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

# enable TLS for secure connection
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# set username and password
client.username_pw_set(os.getenv('MQTT_USER', ''), os.getenv('MQTT_PASSWORD', ''))
# connect to HiveMQ Cloud on port 8883 (default for MQTT)
client.connect(os.getenv('MQTT_CLIENT', ''), 8883)

# setting callbacks, use separate functions like above for better visibility
client.on_publish = on_publish

# subscribe to all topics of encyclopedia by using the wildcard "#"
# client.subscribe("encyclopedia/#", qos=1)

# a single publish, this can also be done in loops, etc.
client.publish("uaic/savana/lion-house-01", payload=json.dumps({
    "event_type": "reading",
    "timestamp": int(time.time()*1000),
    "location": "lion-house-01",
    "data": [
        {
            "sensor_id": 0x1,
            "value": 123
        },
        {
            "sensor_id": 0x2,
            "value": 32.0
        },
        {
            "sensor_id": 0x3,
            "value": 33.2
        }
    ]
}), qos=1)

# loop_forever for simplicity, here you need to stop the loop manually
# you can also use loop_start and loop_stop
client.loop_start()
client.loop_stop()