"""
Author: Kiran Jojare
Email: kijo7257@colorado.edu
Date: June 20, 2024
Version: 1.0

Description:
This code demonstrates how to generate PWM signals to control the brightness of an LED on the Raspberry Pi Pico RP2040.
The LED is connected to GPIO pin 25 (built-in LED).
"""

import time
from machine import Pin, PWM

# Define the LED pin
led = PWM(Pin(25))
led.freq(1000)  # Set frequency to 1 kHz

while True:
    for duty in range(0, 65536, 256):  # Increase duty cycle
        led.duty_u16(duty)
        time.sleep(0.01)
    for duty in range(65535, -1, -256):  # Decrease duty cycle
        led.duty_u16(duty)
        time.sleep(0.01)
