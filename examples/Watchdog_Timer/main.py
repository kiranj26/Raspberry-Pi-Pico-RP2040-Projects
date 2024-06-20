"""
Author: Kiran Jojare
Email: kijo7257@colorado.edu
Date: June 20, 2024
Version: 1.0

Description:
This code demonstrates how to use the Watchdog Timer on the Raspberry Pi Pico RP2040.
The watchdog timer is set up to reset the system if it is not fed within a certain period.
"""

import time
from machine import WDT, Pin

# Initialize the watchdog timer to reset the system after 5 seconds
wdt = WDT(timeout=5000)

# Define the LED pin
led = Pin(25, Pin.OUT)

while True:
    # Simulate normal operation
    led.toggle()
    print("System running normally, feeding the watchdog...")
    wdt.feed()  # Feed the watchdog to prevent system reset
    time.sleep(1)
    
    # Uncomment the following lines to simulate a system hang and observe the watchdog reset
    # print("Simulating system hang...")
    # time.sleep(10)
