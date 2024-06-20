"""
Author: Kiran Jojare
Email: kijo7257@colorado.edu
Date: June 20, 2024
Version: 1.0

Description:
This code demonstrates how to use timers and interrupts on the Raspberry Pi Pico RP2040.
An LED is toggled in a timer interrupt.
"""

import time
from machine import Timer, Pin

# Define the LED pin
led = Pin(25, Pin.OUT)

# Define the timer
timer = Timer()

# Timer interrupt handler
def toggle_led(timer):
    led.toggle()

# Initialize the timer to call the handler every 500ms
timer.init(freq=2, mode=Timer.PERIODIC, callback=toggle_led)

while True:
    time.sleep(1)  # Main loop doing nothing
