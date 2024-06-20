"""
Author: Kiran Jojare
Email: kijo7257@colorado.edu
Date: June 20, 2024
Version: 1.0

Description:
This code demonstrates how to read input from a button and control an LED using GPIO pins on the Raspberry Pi Pico RP2040.
The LED is connected to GPIO pin 25 (built-in LED).
The button is connected to GPIO pin 14.
"""

import time
from machine import Pin

# Define the LED and button pins
led = Pin(25, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value() == 1:
        led.value(1)  # Turn on the LED
    else:
        led.value(0)  # Turn off the LED
    time.sleep(0.1)  # Debounce delay
