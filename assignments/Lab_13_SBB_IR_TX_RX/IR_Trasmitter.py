"""
Author: Kiran Jojare
Email: kijo7257@colorado.edu
Date: June 20, 2024
Version: 1.0

Description:
This code demonstrates how to send IR signals using the Raspberry Pi Pico and an IR LED. The code uses the `ir_tx` library to send NEC protocol commands.
"""

from machine import Pin
import uasyncio as asyncio
from ir_tx.nec import NEC

# Define an asynchronous function to handle IR transmission
async def transmit_ir():
    ir_transmitter = NEC(Pin(17, Pin.OUT, value=0))  # Initialize IR transmitter on Pin 17
    addr = 0x01  # Example device address

    commands = [0x01, 0x02, 0x03, 0x04]  # List of commands to send

    while True:
        for command in commands:
            ir_transmitter.transmit(addr, command)  # Send each command
            print(f"IR signal transmitted: Addr {addr} Command {command}")
            await asyncio.sleep(3)  # Wait for 3 seconds before sending the next command

# Main function to run the transmitter
async def main():
    await transmit_ir()  # Call the transmit function

if __name__ == "__main__":
    asyncio.run(main())  # Start the asynchronous event loop
