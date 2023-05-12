# TC1001S

## Members:
- Leader: Kirill Makienko Tkachenko (A01425218)
- Participant: Dulce Nahomi Bucio Rivas (A01425284)
- Supervisor: Oscar Omar Zepeda Vázquez (A01425397)

---

### Content

1. [Python MQTT Client](#python-mqtt-client)
2. [Used Libraries](#used-libraries)
3. [Constants](#constants)
4. [Functions](#functions)
5. [Usage](#usage)
6. [Sending and Recieving Messages](#sending-and-recieving-messages)

### Python MQTT Client

This code provides a Python implementation of an MQTT client for sending and receiving messages using MQTT. this program allows the client to connect to an MQTT broker, publish messages to a specific topic, and subscribe to topics to receive messages.

### Used Libraries

This code relies on the following libraries:

- sys: Provides access to system-specific parameters and functions.
- paho.mqtt.client: The "Paho MQTT Python client" library for connecting to an MQTT broker.
- random: Generates a random number between two numbers. Used frecuently for client's ID.
- time: Using functions, the "time" client library counts the number of seconds.

Make sure you have these libraries installed before running the code.

### Constants

- port: Port used for MQTT broker to run.
- client_id: String containing a randomized user ID.

### Functions

- descifrar_orden(): Function to assign values despite the order of the command line.
- connect_mqtt(): Function that connects the client to the IP.
- publish(): Function to publish a message in a topic.
- suscribe(): Function to suscribe the client and receive messages.
- on_connect(): Function that return the connection state.
- on_message(): Function that writes the recieved message.

### Usage

The code supports two main operations: sending messages and subscribing to topics.

### Sending and Recieving Messages

To send messages, use the following command line syntax:

```
py mqtt_client.py send -p <broker> -c <topic> -m <message>
```

Meanwhile, to recive the messages, use the following command line syntax:

```
py Main.py subscribe -c Marco -p 18.208.155.95
```

---