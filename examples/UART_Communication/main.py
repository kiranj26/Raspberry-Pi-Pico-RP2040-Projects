"""
Author: Kiran Jojare
Email: kijo7257@colorado.edu
Date: June 20, 2024
Version: 1.0

Description:
This code demonstrates how to use UART communication on the Raspberry Pi Pico RP2040.
The example sends and receives data over UART.
"""

from machine import UART, Pin
import time

# Initialize UART1
uart1 = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))

# Function to send a message
def send_message(message):
    uart1.write(message + '\n')

# Function to receive a message
def receive_message():
    if uart1.any():
        message = uart1.read().decode('utf-8')
        return message
    return None

while True:
    send_message("Hello, UART!")
    time.sleep(1)
    
    received = receive_message()
    if received:
        print("Received:", received)
    time.sleep(1)
