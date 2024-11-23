import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt


BEAM_PIN = 17

ID_PARKING = "PARKING_1"
MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_TOPIC = "lechuga/parking"
MQTT_CLIENT_ID = "RaspberryPi_BeamMonitor"

# Inicializar el cliente MQTT
client = mqtt.Client(MQTT_CLIENT_ID)


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


def break_beam_callback(channel):
    if GPIO.input(BEAM_PIN):
        status = False
    else:
        status = True

    try:
        if status:
            client.publish(MQTT_TOPIC, ID_PARKING)
            print(f"Car detected")
    except Exception as e:
        print(f"MQTT publish error: {e}")


GPIO.setmode(GPIO.BCM)
GPIO.setup(BEAM_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(BEAM_PIN, GPIO.BOTH,
                      callback=break_beam_callback, bouncetime=200)

try:
    message = input("Press enter to exit\n\n")
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
    client.loop_stop()
    client.disconnect()
