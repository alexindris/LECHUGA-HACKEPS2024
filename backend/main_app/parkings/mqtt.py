from typing import Any
from main_app.parkings.actions import create_parking_entry
from main_app.parkings.models import EntryType
import paho.mqtt.client as mqtt
from infrastructure.viewer_context.viewer_context import AllPowerfulViewerContext
from hackathon.settings import MQTT_HOST, MQTT_PORT, MQTT_TOPIC
import json


def on_connect(client: mqtt.Client, userdata: Any, flags: Any, rc: int) -> None:
    if rc == 0:
        print("Connected to MQTT Broker!")
        client.subscribe(MQTT_TOPIC)
    else:
        print(f"Failed to connect, return code {rc}")


def on_message(client: mqtt.Client, userdata: Any, msg: mqtt.MQTTMessage) -> None:
    vc = AllPowerfulViewerContext(None)
    if msg.topic == MQTT_TOPIC:
        data = msg.payload.decode()

        entry = json.loads(data)

        parkin_id = entry.get("parking_id")
        entry_type = entry.get("entry_type")

        if entry_type == "ENTRANCE":
            entry_type = EntryType.ENTRANCE
        else:
            entry_type = EntryType.EXIT

        create_parking_entry(vc, parkin_id, entry_type)
    print(f"Received message from topic {msg.topic}: {msg.payload.decode()}")


def start_mqtt() -> None:
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        client.connect(MQTT_HOST, MQTT_PORT)
        client.loop_start()
    except Exception as e:
        print(f"Error connecting to MQTT Broker: {e}")
