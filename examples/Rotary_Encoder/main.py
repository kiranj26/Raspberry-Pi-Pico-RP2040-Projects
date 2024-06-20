"""
Author: Kiran Jojare
Email: kijo7257@colorado.edu
Date: June 20, 2024
Version: 1.0

Description:
This code demonstrates how to use a rotary encoder with the Raspberry Pi Pico RP2040.
The rotary encoder is connected to GPIO pins 14 and 15.
"""

from machine import Pin
import time

# Define the rotary encoder pins
pin_a = Pin(14, Pin.IN, Pin.PULL_UP)
pin_b = Pin(15, Pin.IN, Pin.PULL_UP)

# Variables to store the current and previous states
last_state = pin_a.value()
position = 0

def rotary_encoder():
    global last_state, position
    current_state = pin_a.value()
    if current_state != last_state:
        if pin_b.value() != current_state:
            position += 1
        else:
            position -= 1
        print("Position:", position)
    last_state = current_state

# Attach an interrupt to the rotary encoder pin
pin_a.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=lambda pin: rotary_encoder())

while True:
    time.sleep(1)  # Main loop doing nothing
