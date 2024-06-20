"""
Author: Kiran Jojare
Email: kijo7257@colorado.edu
Date: June 20, 2024
Version: 1.0

Description:
This code demonstrates how to use the ADC (Analog-to-Digital Converter) with interrupts on the Raspberry Pi Pico RP2040.
The potentiometer is connected to GPIO pin 26 (ADC0).
"""

import time
from machine import ADC, Timer, Pin

# Define the ADC pin
adc_pin = ADC(Pin(26))
led = Pin(25, Pin.OUT)

# Variable to store the ADC result
adc_result = 0

# Timer interrupt handler
def read_adc(timer):
    global adc_result
    adc_result = adc_pin.read_u16()
    if adc_result > 32768:
        led.value(1)
    else:
        led.value(0)

# Define the timer
timer = Timer()

# Initialize the timer to call the handler every 500ms
timer.init(freq=2, mode=Timer.PERIODIC, callback=read_adc)

while True:
    print("ADC Result:", adc_result)
    time.sleep(1)
