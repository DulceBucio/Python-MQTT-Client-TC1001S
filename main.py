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


