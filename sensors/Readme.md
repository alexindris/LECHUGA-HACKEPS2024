# Parking Sensor and Simulation Project

## Overview
This scripts are designed to monitor and manage the capacity of a parking lot in real time using MQTT messaging. It consists of two Python scripts:

- **`sensor.py`**: The primary script, intended to run on a Raspberry Pi connected to an infrared sensor, detects cars entering. It reports events to an MQTT broker to enable real-time tracking of parking space availability.
- **`simulation.py`**: A testing utility that simulates car detections by publishing randomized car events to the same MQTT broker, eliminating the need for physical hardware during development or testing phases.

---

## Key Functionality

### `sensor.py` - Parking Access Control
- **Purpose**: Control the access of vehicles to a parking lot using an infrared beam sensor connected to a Raspberry Pi.
- **How It Works**:
  - Detects interruptions in the beam caused by cars entering or leaving the parking lot.
  - Publishes an event to a pre-configured MQTT broker and topic (`lechuga/parking`) with the parking lot ID (`PARKING_1`).
  - Utilizes GPIO functionality to monitor the sensor and ensures proper cleanup upon exit.
- **Use Case**: Real-time monitoring of parking lot capacity in an operational environment.

### `simulation.py` - Testing Utility
- **Purpose**: Simulate parking lot activity for testing the MQTT integration and external systems without requiring physical hardware.
- **How It Works**:
  - Generates randomized "car detected" events at intervals between 5 and 60 seconds.
  - Publishes events to the same MQTT broker and topic (`lechuga/parking`) with a different parking lot ID (`PARKING_0`).
- **Use Case**: Validate the system’s functionality and message handling in controlled, repeatable scenarios.

---

## Why `sensor.py` is Essential
The core of the project lies in `sensor.py`, which uses a Raspberry Pi and an infrared sensor to manage parking access:

1. **Hardware Integration**: The script directly interfaces with the Raspberry Pi GPIO pins to detect real-world events (beam breaks caused by vehicle movement).
2. **Real-Time Communication**: Relays events to an MQTT broker, enabling live updates on parking capacity.
3. **Low-Cost Solution**: Leverages affordable hardware for scalable and efficient parking management.

`simulation.py` supports testing by replicating this behavior without needing a physical setup, but the primary operational focus remains on the functionality provided by `sensor.py`.

---

## System Requirements

### For `sensor.py`:
- Raspberry Pi (any model with GPIO support)
- Infrared beam sensor (or similar detection hardware)
- Python 3 with the following libraries:
  - `RPi.GPIO`
  - `paho-mqtt`

### For `simulation.py`:
- Any system running Python 3
- The `paho-mqtt` library

---

## How to Use

### Setting Up `sensor.py`
1. **Hardware Configuration**:
   - Connect the infrared sensor to the Raspberry Pi GPIO pin specified in the script (default is pin 17).
   - Ensure proper wiring and pull-up/down resistor configuration.
2. **Install Dependencies**:
   ```bash
   sudo apt-get install python3-rpi.gpio
   pip install paho-mqtt
   ```
3. **Run the Script**:
   ```bash
   python3 sensor.py
   ```
   The script will continuously monitor the sensor and publish car detection events to the MQTT broker.

### Setting Up `simulation.py`
1. **Install Dependencies**:
   ```bash
   pip install paho-mqtt
   ```
2. **Run the Script**:
   ```bash
   python3 simulation.py
   ```
   This script will generate simulated car detection events at random intervals for testing.

---

## MQTT Configuration
Both scripts rely on MQTT for communication. Default settings are:

- **Broker**: `test.mosquitto.org`
- **Port**: `1883`
- **Topic**: `lechuga/parking`

You can modify these values in the scripts to match your MQTT setup.

---


### Authors
Created by Lechuga 🥬