import json
from datetime import datetime

TRANSFORM_PREFIX = "openhab/smartmeter"


def transform(message: object):
    """Performs the message harmonization.

    Args:
        message

    Returns:
        object
    """
    topic = message.topic

    if "gPlug" in topic and "SENSOR" in topic:
        name = topic.split("/")[1]
        name = map_name(name)
        data = json.loads(message.payload)
        [field, value] = list(data["z"].items())[0]
        time = int(datetime.now().timestamp())
        new_field = map_field("DSMR", field)
        return [name, time, new_field, value]

    if "smartmeter/" in topic:
        name = topic.split("/")[1]
        name = map_name(name)
        data = json.loads(message.payload)
        value = data["value"]
        time = int(datetime.now().timestamp())
        field = topic.split("/")[2]
        new_field = map_field("DLMS", field)
        return [name, time, new_field, value]

    raise Exception("Not sensor data.")


def format_msg(name, time, field, value):
    """Formats MQTT message a json string.
    """
    topic = f"{TRANSFORM_PREFIX}/{name}/{field}"
    msg = json.dumps({
        "time": time,
        "value": value
    })
    return topic, msg


def map_name(name):
    """Maps device name to new device name.
    """
    if "12345" in name:
        return "AEW"
    if "LG" in name:
        return "EKZ"
    if "gPlug10" in name:
        return "EWB"
    if "gPlug11" in name:
        return "ROM"


def map_field(device, field):
    if device == "DSMR":
        if field == "Ei":
            return "energy_in"
        if field == "Ei1":
            return "energy_in"
        if field == "Ei2":
            return "energy_in/tariff_2"
        if field == "Eo":
            return "energy_out"
        if field == "Eo1":
            return "energy_out"
        if field == "Pi":
            return "power_in"
        if field == "Po":
            return "power_out"
        if field == "P1i":
            return "power_in"
    if device == "DLMS":
        if field == "ACTIVE_POWER_P":
            return "power_in"
        if field == "ACTIVE_POWER_N":
            return "power_out"
        if field == "ACTIVE_ENERGY_P":
            return "energy_in"
        if field == "ACTIVE_ENERGY_N":
            return "energy_out"
    return "extra:"+field
