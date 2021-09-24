import paho.mqtt.client as mqttClient
from transformer import transform

BROKER_ENDP = "192.168.1.100"
BROKER_PORT = 1883
BROKER_USER = "hackday"
BROKER_PASS = "hadkday"


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
user = "hackday"                    # Connection username
password = "hackday"                # Connection password


client = mqttClient.Client("jonas_python_mqtt")
client.username_pw_set(BROKER_USER, password=BROKER_PASS)
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER_ENDP, BROKER_PORT, 60)
client.loop_forever()
