import paho.mqtt.client as mqttClient
import datetime
import csv
import json


def on_connect(client, userdata, flags, rc):

    if rc == 0:
        print("Connected to broker")
        global Connected                # Use global variable
        Connected = True                # Signal connection
    else:
        print("Connection failed")


def on_message(client, userdata, message):

    # print("Message received!")
    print(message.payload)

    # take [2:-1] to remove b and quotes (b'...') at the left and right side
    try:
        message_payload_decoded = json.loads(str(message.payload))
        print(message_payload_decoded)
    except:
        print("Message not json parsable")


Connected = False   # global variable for the state of the connection

broker_address = "10.19.103.106"    # Broker address
port = 1883                         # Broker port
user = "hackday"                  # Connection username
password = "hackday"              # Connection password

topic = "#"

client = mqttClient.Client("jonas_python_mqtt")          # create new instance
client.username_pw_set(user, password=password)     # set username and password
client.on_connect = on_connect                      # attach function to callback
client.on_message = on_message                      # attach function to callback
client.connect(broker_address, port, 10)            # connect
client.subscribe(topic)                             # subscribe
client.loop_forever()                               # then keep listening forever
