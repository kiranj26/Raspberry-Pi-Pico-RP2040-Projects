"""
Author: Kiran Jojare
Email: kijo7257@colorado.edu
Date: June 20, 2024
Version: 1.0

Description:
This code demonstrates how to blink an LED connected to the Raspberry Pi Pico RP2040.
The LED is connected to GPIO pin 25 (built-in LED).
"""

import time
from machine import Pin

# Define the LED pin
led = Pin(25, Pin.OUT)

while True:
    led.value(1)  # Turn on the LED
    time.sleep(1)  # Wait for 1 second
    led.value(0)  # Turn off the LED
    time.sleep(1)  # Wait for 1 second
