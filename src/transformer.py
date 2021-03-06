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

    if "M1" in topic and "SENSOR" in topic:
        name = topic.split("/")[1]
        name = map_name(name)
        data = json.loads(message.payload)
        time = int(datetime.now().timestamp())
        [field, value] = list(data["Z1"].items())[0]
        new_field = map_field("GPLUG_PROTO1", field)
        return [name, time, new_field, value]

    if "gPlug" in topic and "SENSOR" in topic:
        name = topic.split("/")[1]
        name = map_name(name)
        data = json.loads(message.payload)
        [field, value] = list(data["z"].items())[0]
        time = int(datetime.now().timestamp())
        new_field = map_field("GPLUG_PROTO2", field)
        return [name, time, new_field, value]

    if "smartmeter/" in topic:
        name = topic.split("/")[1]
        name = map_name(name)
        data = json.loads(message.payload)
        value = data["value"]
        time = int(datetime.now().timestamp())
        field = topic.split("/")[2]
        new_field = map_field("EKZ_PROTO", field)
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
    if "M1" in name:
        return "BKW"
    if "LG" in name:
        return "EKZ"
    if "gPlug10" in name:
        return "EWB"
    if "gPlug11" in name:
        return "ROM"


def map_field(device, field):
    if device == "GPLUG_PROTO1":
        if field == "P_Bezug":
            return "power_in"
        if field == "P_Ein":
            return "power_out"
    if device == "GPLUG_PROTO2":
        if field in ["Ei", "Ei1"]:
            return "energy_in"
        if field in ["Eo", "Eo1"]:
            return "energy_out"
        if field == "Pi":
            return "power_in"
        if field == "Po":
            return "power_out"
        if field == "P1i":
            return "power_in"
    if device == "EKZ_PROTO":
        if field == "ACTIVE_POWER_P":
            return "power_in"
        if field == "ACTIVE_POWER_N":
            return "power_out"
        if field == "ACTIVE_ENERGY_P":
            return "energy_in"
        if field == "ACTIVE_ENERGY_N":
            return "energy_out"

    return "extra:"+field
