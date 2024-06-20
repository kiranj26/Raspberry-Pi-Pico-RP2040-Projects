"""
Author: Kiran Jojare
Email: kijo7257@colorado.edu
Date: June 20, 2024
Version: 1.0

Description:
This code demonstrates how to use external interrupts on the Raspberry Pi Pico RP2040.
An LED is toggled when a button press triggers an interrupt.
"""

import time
from machine import Pin

# Define the LED and button pins
led = Pin(25, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

# Interrupt handler function
def handle_interrupt(pin):
    led.toggle()

# Attach the interrupt to the button pin
button.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)

while True:
    time.sleep(1)  # Main loop doing nothing
