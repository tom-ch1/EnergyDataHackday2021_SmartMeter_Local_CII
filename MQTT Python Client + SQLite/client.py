import paho.mqtt.client as mqttClient
from transformer import transform
from influxdb import InfluxDBClient

BROKER_ENDP = "192.168.1.100"
BROKER_PORT = 1883
BROKER_USER = "hackday"
BROKER_PASS = "hadkday"

INFLUXDB_ADDRESS = '192.168.1.100'
INFLUXDB_USER = 'mqtt'
INFLUXDB_PASSWORD = 'mqtt'
INFLUXDB_DATABASE = 'smartmeter'

# influxdb_client = InfluxDBClient(
#     INFLUXDB_ADDRESS, 8086, INFLUXDB_USER, INFLUXDB_PASSWORD, None)


def on_connect(client, userdata, flags, rc):
    print("Connected to the broker..")
    client.subscribe("smartmeter/#")


def on_message(client, userdata, message):
    print(message)
    print(message.payload)
    if "Online" in str(message.payload):
        return

    topic, payload = transform(message)

    # # if topic and payload:
    # #     client.publish(topic, payload)
    # influxdb_client.write_points(payload)
    # print("sent to influxdb")


broker_address = "192.168.1.100"    # Broker address
port = 1883                         # Broker port
user = "hackday"                    # Connection username
password = "hackday"                # Connection password


client = mqttClient.Client("Jackson")
client.username_pw_set(BROKER_USER, password=BROKER_PASS)
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER_ENDP, BROKER_PORT, 60)
client.loop_forever()
