import time
import random
import paho.mqtt.client as mqtt
import json

ID_PARKING = "b1b7cac2-3a16-4231-aa0a-a431588e8d03"
ENTRY_TYPE = "ENTRANCE" 
MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_TOPIC = "lechuga/parking"
MQTT_CLIENT_ID = "RaspberryPi_ParkingSimulator"

client = mqtt.Client(client_id=MQTT_CLIENT_ID, protocol=mqtt.MQTTv311)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("MQTT connected")
    else:
        print(f"MQTT failed with code {rc}")


client.on_connect = on_connect

try:
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
except Exception as e:
    print(f"MQTT unreachable: {e}")
    exit(1)

client.loop_start()

try:
    print("Starting vehicle simulation...\n")
    vehicle_count = 0

    while True:
        time_to_wait = random.uniform(5, 60)
        time.sleep(time_to_wait)

        vehicle_count += 1
        try:
            payload = {
            "parking_id": ID_PARKING,
            "entry_type": ENTRY_TYPE
            }
            payload_json = json.dumps(payload)
            client.publish(MQTT_TOPIC, payload_json)
            print(payload_json)
        except Exception as e:
            print(f"MQTT publish error: {e}")

    try:
        message = input("Press enter to exit\n\n")
    except KeyboardInterrupt:
        pass
finally:
    client.loop_stop()
    client.disconnect()
