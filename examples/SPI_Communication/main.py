"""
Author: Kiran Jojare
Email: kijo7257@colorado.edu
Date: June 20, 2024
Version: 1.0

Description:
This code demonstrates how to communicate with an SPI device using the Raspberry Pi Pico RP2040.
The example reads data from an SPI flash memory (e.g., W25Q32) connected to the SPI bus.
"""

from machine import Pin, SPI
import time

# Define SPI pins
spi = SPI(0, baudrate=1000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(19), miso=Pin(16))
cs = Pin(17, Pin.OUT)

def read_flash_id():
    cs.value(0)
    spi.write(bytes([0x9F]))
    flash_id = spi.read(3)
    cs.value(1)
    return flash_id

while True:
    flash_id = read_flash_id()
    print("Flash ID:", flash_id)
    time.sleep(1)
