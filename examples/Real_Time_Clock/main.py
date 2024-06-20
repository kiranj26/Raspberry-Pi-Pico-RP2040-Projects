"""
Author: Kiran Jojare
Email: kijo7257@colorado.edu
Date: June 20, 2024
Version: 1.0

Description:
This code demonstrates how to use the Real-Time Clock (RTC) on the Raspberry Pi Pico RP2040.
It sets the current time and then prints the time every second.
"""

import time
import machine

# Define the RTC
rtc = machine.RTC()

# Set the current time: year, month, day, weekday, hours, minutes, seconds, subseconds
rtc.datetime((2024, 6, 20, 4, 12, 0, 0, 0))

while True:
    # Get the current time
    current_time = rtc.datetime()
    
    # Print the current time
    print("Current time: {}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(
        current_time[0], current_time[1], current_time[2],
        current_time[4], current_time[5], current_time[6]
    ))
    
    time.sleep(1)
