import time
import random
import paho.mqtt.client as mqtt
import json

SENSOR_IDS = [
    "b1b7cac23a164231aa0aa431588e8d03",
    "f60148ca14d74b3e8b07ceb9eddddc4f",
    "cd64ea32a2284e99b79c5747d29ab96a"
]

MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_TOPIC = "lechuga/parking"
MQTT_CLIENT_ID = "RaspberryPi_ParkingSimulator"

MAX_PARKING_CAPACITY = 50

client = mqtt.Client(client_id=MQTT_CLIENT_ID, protocol=mqtt.MQTTv311)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT successfully")
    else:
        print(f"Failed to connect to MQTT with code {rc}")

client.on_connect = on_connect

try:
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
except Exception as e:
    print(f"MQTT unreachable: {e}")
    exit(1)

client.loop_start()

try:
    print("Starting vehicle simulation...\n")
    
    vehicles_in_parking = {sensor_id: 0 for sensor_id in SENSOR_IDS}

    while True:
        time_to_wait = random.uniform(2, 15)
        time.sleep(time_to_wait)

        selected_sensor = random.choice(SENSOR_IDS)
        current_count = vehicles_in_parking[selected_sensor]
        
        if (current_count > 0 and random.random() < 0.3) or current_count >= MAX_PARKING_CAPACITY:
            entry_type = "EXIT"
            vehicles_in_parking[selected_sensor] -= 1
        else:
            entry_type = "ENTRANCE"
            vehicles_in_parking[selected_sensor] += 1

        try:
            payload = {
                "parking_id": selected_sensor,
                "entry_type": entry_type,
                "current_count": vehicles_in_parking[selected_sensor]
            }
            payload_json = json.dumps(payload)
            client.publish(MQTT_TOPIC, payload_json)
            print(f"Published: {payload_json}")
        except Exception as e:
            print(f"MQTT publish error: {e}")

except KeyboardInterrupt:
    print("\nSimulation terminated by user.")

finally:
    client.loop_stop()
    client.disconnect()
    print("Disconnected from MQTT.")
