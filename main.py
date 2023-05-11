# Used libraries
import sys
from paho.mqtt import client as mqtt_client
import random

# Constants 
port = 1883 # Port that we will always use
client_id = f'python-mqtt-{random.randint(0, 1000)}' # Randomized ID for the client

# Function to assign values despite the order of the command line
def descifrar_orden(argv):
    for i in range(len(argv)-1):
        
        if argv[i] == "-p":
            broker = argv[i+1]
        
        if argv[i] == "-c":
            topic = argv[i+1]
        
        if argv[1] == "send":
            if argv[i] == "-m":
                message = argv[i+1]
    if argv[1] == "send":
        return[broker,topic,message]
    else:
        return[broker,topic]


# Function to publish a message in a topic
def publish(client, topic, msg):
    msg_count = 0
    while True:
        result = client.publish(topic, msg)
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
            break
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1


# Function to suscribe the client and receive messages
def subscribe(client: mqtt_client, topic):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message