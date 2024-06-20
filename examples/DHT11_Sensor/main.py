"""
Author: Kiran Jojare
Email: kijo7257@colorado.edu
Date: June 20, 2024
Version: 1.0

Description:
This code demonstrates how to use the DHT11 temperature and humidity sensor with the Raspberry Pi Pico RP2040.
The DHT11 sensor is connected to GPIO pin 16.
"""

import time
import dht
from machine import Pin

# Define the DHT11 sensor pin
sensor = dht.DHT11(Pin(16))

while True:
    try:
        # Measure the temperature and humidity
        sensor.measure()
        temp = sensor.temperature()
        humidity = sensor.humidity()
        
        # Print the values
        print("Temperature: {}°C  Humidity: {}%".format(temp, humidity))
    except OSError as e:
        print("Failed to read sensor.")
    
    time.sleep(2)
