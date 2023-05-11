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

# Function that connects the client to the IP
def connect_mqtt(broker):
    # Function that return the connection state
    def on_connect(
            client, userdata, flags, 
            rc): 
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id) # Assigns Client ID 
    client.on_connect = on_connect
    client.connect(broker, port) # Establish the connection with the server
    return client 


# Function that connects to the mqtt client 
def connect_mqtt(broker) -> mqtt_client:
    def on_connect(
            client, userdata, flags, 
            rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client