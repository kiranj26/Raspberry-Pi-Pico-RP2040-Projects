"""
Author: Kiran Jojare
Email: kijo7257@colorado.edu
Date: June 20, 2024
Version: 1.0

Description:
This code demonstrates how to use PWM to control a servo motor on the Raspberry Pi Pico RP2040.
The servo is connected to GPIO pin 15.
"""

import time
from machine import Pin, PWM

# Define the servo pin
servo = PWM(Pin(15))
servo.freq(50)  # Set frequency to 50 Hz for servo control

# Function to set servo angle
def set_servo_angle(angle):
    # Map angle (0-180) to PWM duty cycle (1000-9000)
    duty = int((angle / 180 * 8000) + 1000)
    servo.duty_u16(duty)

while True:
    # Sweep the servo from 0 to 180 degrees
    for angle in range(0, 181, 5):
        set_servo_angle(angle)
        time.sleep(0.02)
    # Sweep the servo back from 180 to 0 degrees
    for angle in range(180, -1, -5):
        set_servo_angle(angle)
        time.sleep(0.02)
