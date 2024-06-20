"""
Author: Kiran Jojare
Email: kijo7257@colorado.edu
Date: June 20, 2024
Version: 1.0

Description:
This code demonstrates how to use an OLED display (SSD1306) with the Raspberry Pi Pico RP2040.
The OLED display is connected to the I2C bus (GPIO pins 4 and 5).
"""

import machine
import ssd1306
import time

# Define I2C pins and initialize I2C
i2c = machine.I2C(0, scl=machine.Pin(5), sda=machine.Pin(4), freq=400000)

# Initialize the OLED display
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

while True:
    # Clear the display
    oled.fill(0)
    
    # Display text
    oled.text("Hello, World!", 0, 0)
    oled.text("Raspberry Pi Pico", 0, 10)
    oled.text("SSD1306 OLED", 0, 20)
    
    # Update the display
    oled.show()
    
    # Wait for 2 seconds
    time.sleep(2)
    
    # Clear the display
    oled.fill(0)
    
    # Display text
    oled.text("Displaying time:", 0, 0)
    oled.text(time.strftime("%H:%M:%S"), 0, 10)
    
    # Update the display
    oled.show()
    
    # Wait for 2 seconds
    time.sleep(2)
