import paho.mqtt.client as mqttClient
from transformer import transform


def on_connect(client, userdata, flags, rc):
    print("Connected")
    client.subscribe("#")


def on_message(client, userdata, message):

    print(message.payload)
    if "Online" in str(message.payload):
        return

    topic, payload = transform(message)

    if topic and payload:
        client.publish(topic, payload)


broker_address = "192.168.1.100"    # Broker address
port = 1883                         # Broker port
user = "hackday"                  # Connection username
password = "hackday"              # Connection password


client = mqttClient.Client("jonas_python_mqtt")          # create new instance
client.username_pw_set(user, password=password)     # set username and password
# attach function to callback
client.on_connect = on_connect
# attach function to callback
client.on_message = on_message
client.connect(broker_address, port, 60)            # connect
# subscribe
client.loop_forever()                               # then keep listening forever
