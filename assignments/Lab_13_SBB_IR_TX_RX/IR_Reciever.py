"""
Author: Kiran Jojare
Email: kijo7257@colorado.edu
Date: June 20, 2024
Version: 1.0

Description:
This code demonstrates how to use the Adafruit TSOP382 IR receiver with the Raspberry Pi Pico to decode IR signals using the NEC protocol. The code sets up the IR receiver, captures IR signals, and decodes them into actionable commands.
"""

from machine import Pin
import uasyncio as asyncio
from ir_rx.nec import NEC_8  # Use the NEC 8-bit class

# Initialize GPIO pins for LEDs with corresponding command codes
led_pins = {
   0x01: Pin(18, Pin.OUT),  # Command 0x01 associated with LED on Pin 18
   0x02: Pin(19, Pin.OUT),  # Command 0x02 associated with LED on Pin 19
   0x03: Pin(20, Pin.OUT),  # Command 0x03 associated with LED on Pin 20
   0x04: Pin(21, Pin.OUT)   # Command 0x04 associated with LED on Pin 21
}

# Asynchronous function to turn off LED after a delay
async def turn_off_led(led_pin):
   await asyncio.sleep(2)  # Non-blocking wait for 2 seconds
   led_pin.value(0)  # Turn off LED

# Callback function triggered when an IR code is received
async def ir_callback(data, addr, _):
   print(f"Received NEC command! Data: 0x{data:02X} Addr: 0x{addr:02X}")
   if data in led_pins:  # If the command is one of the known commands
       led_pin = led_pins[data]  # Get the corresponding LED Pin object
       led_pin.value(1)  # Turn on the LED
       asyncio.create_task(turn_off_led(led_pin))  # Schedule turning off the LED

# Initialize and set up the IR receiver
ir_pin = Pin(16, Pin.IN, Pin.PULL_UP)  # IR receiver on GPIO Pin 16
ir_receiver = NEC_8(ir_pin, callback=ir_callback)  # Setup IR receiver with the callback function `ir_callback`.

# Optional use print_error for debugging if necessary
ir_receiver.error_function(print_error)

# Asynchronous main loop to keep the script running
async def main():
    while True:
        await asyncio.sleep_ms(100)  # Sleep for 100 ms

# Run the asynchronous event loop
if __name__ == "__main__":
    asyncio.run(main())
