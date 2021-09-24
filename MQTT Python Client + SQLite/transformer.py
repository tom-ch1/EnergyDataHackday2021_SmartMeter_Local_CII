import json


def transform(message):
    topic = message.topic
    if "tele/gPlug" in topic:
        data = json.loads(message.payload)
        [field, value] = list(data["z"].items())[0]
        value = data["z"][field]
        name = topic.split("/")[1]
        time = data["Time"]
        return format_msg(name, time, field, value)

    if "smartmeter/" in topic:
        name = topic.split("/")[1]
        data = json.loads(message.payload)
        value = data["value"]
        time = data["timestamp"]
        field = topic.split("/")[2]
        new_field = mapping("EKZ", field)
        return format_msg(name, time, new_field, value)

    return None, None


def format_msg(name, time, field, value):
    topic = f"grafana/{name}/{field}"
    payload = json.dumps(
        {
            'measurement': field,
            "tags": {
                "timestamp": time
            },
            "fields": {
                field: value
            }
        }
    )
    return topic, payload


def mapping(device, field):
    if device == "EKZ":
        if field == "ACTIVE_POWER_P":
            return "Pi"
        if field == "ACTIVE_POWER_N":
            return "Po"
        if field == "CURRENT_L1":
            return "I1"
        if field == "CURRENT_L2":
            return "I2"
        if field == "CURRENT_L3":
            return "I3"
        if field == "VOLTAGE_L3":
            return "I3"

    return field
