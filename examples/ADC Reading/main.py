"""
Author: Kiran Jojare
Email: kijo7257@colorado.edu
Date: June 20, 2024
Version: 1.0

Description:
This code demonstrates how to read analog values from a potentiometer or sensor using the ADC (Analog-to-Digital Converter) on the Raspberry Pi Pico RP2040.
The potentiometer is connected to GPIO pin 26 (ADC0).
"""

import time
from machine import ADC, Pin

# Define the ADC pin
pot = ADC(Pin(26))

while True:
    pot_value = pot.read_u16()
    print("Potentiometer value:", pot_value)
    time.sleep(0.5)
