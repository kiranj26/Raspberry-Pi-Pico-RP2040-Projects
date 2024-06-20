"""
Author: Kiran Jojare
Email: kijo7257@colorado.edu
Date: June 20, 2024
Version: 1.0

Description:
This code demonstrates how to communicate with an I2C device using the Raspberry Pi Pico RP2040.
The example reads data from an I2C temperature sensor (e.g., TMP102) connected to the I2C bus.
"""

from machine import Pin, I2C
import time

# Define I2C pins
i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)

# I2C address of the TMP102 sensor
TMP102_ADDR = 0x48

def read_temp():
    data = i2c.readfrom_mem(TMP102_ADDR, 0x00, 2)
    temp_raw = (data[0] << 8) | data[1]
    temp_c = (temp_raw >> 4) * 0.0625
    return temp_c

while True:
    temperature = read_temp()
    print("Temperature:", temperature, "C")
    time.sleep(1)
