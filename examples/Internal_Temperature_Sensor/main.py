"""
Author: Kiran Jojare
Email: kijo7257@colorado.edu
Date: June 20, 2024
Version: 1.0

Description:
This code demonstrates how to use the internal temperature sensor on the Raspberry Pi Pico RP2040.
It reads the temperature from the internal sensor and prints the value every second.
"""

import time
from machine import ADC

# Internal temperature sensor is connected to ADC channel 4
temp_sensor = ADC(4)

def read_internal_temp():
    # Read raw value from the temperature sensor
    raw = temp_sensor.read_u16()
    # Convert the raw value to temperature in degrees Celsius
    # The formula is based on the RP2040 datasheet
    voltage = 3.3 * (raw / 65535)
    temperature = 27 - (voltage - 0.706) / 0.001721
    return temperature

while True:
    temperature = read_internal_temp()
    print("Internal Temperature: {:.2f} °C".format(temperature))
    time.sleep(1)
