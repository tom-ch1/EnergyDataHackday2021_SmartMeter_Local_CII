import paho.mqtt.client as mqttClient
from transformer import transform, format_msg
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client import InfluxDBClient, Point

BROKER_ENDP = "localhost"
BROKER_PORT = 1883
BROKER_USER = "hackday"
BROKER_PASS = "hackday"

INFLUXDB_URL = 'http://localhost:8086'
INFLUXDB_TOKEN = 'OKzVyqE2gv-ykddVAzc3jB6CnVg_UWZ9xhQ7of9JX5YGK2r8B6wFJ9vEtMg7b2JNn5_wE6PhJ_mLGwYMWuAJhw=='
INFLUXDB_ORG = "hackday"
INFLUXDB_BUCKET = "hackday"
INFLUXDB_DATABASE = 'smartmeter'


influxdb_client = InfluxDBClient(
    url=INFLUXDB_URL, token=INFLUXDB_TOKEN, org=INFLUXDB_ORG)
write_api = influxdb_client.write_api(write_options=SYNCHRONOUS)


def on_connect(client, userdata, flags, rc):
    print("Connected to the broker..")
    client.subscribe("#")


def on_message(client, userdata, message):
    if "Online" in str(message.payload):
        return

    if "openhab" in message.topic:
        return

    try:
        payload = transform(message)
        write_point(payload)
        topic, msg = format_msg(*payload)
        client.publish(topic, msg)
    except:
        pass


def write_point(payload):
    [name, time, field, value] = payload
    p = Point(INFLUXDB_DATABASE).tag(
        "name", name).field("time", time).field(field, float(value))
    write_api.write(bucket=INFLUXDB_BUCKET, record=p)


client = mqttClient.Client("Python")
client.username_pw_set(BROKER_USER, password=BROKER_PASS)
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER_ENDP, BROKER_PORT, 60)
client.loop_forever()
