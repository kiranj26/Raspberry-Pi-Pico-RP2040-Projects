"""
Author: Kiran Jojare
Email: kijo7257@colorado.edu
Date: June 20, 2024
Version: 1.0

Description:
This code demonstrates how to control Neopixels (WS2812 LEDs) using the Raspberry Pi Pico RP2040.
It cycles through different colors on a strip of Neopixels connected to GPIO pin 15.
"""

import time
import array
import machine
import rp2

# Configuration parameters for the Neopixel strip
NUM_LEDS = 8  # Number of LEDs in the strip
PIN_NUM = 15  # GPIO pin connected to the Neopixel strip
brightness = 0.1  # Brightness of the LEDs

# Define the Neopixel strip
@rp2.asm_pio(sideset_init=rp2.PIO.OUT_HIGH, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1)                 .side(0)    [T3 - 1]
    jmp(not_x, "do_zero")     .side(1)    [T1 - 1]
    jmp("bitloop")            .side(1)    [T2 - 1]
    label("do_zero")
    nop()                     .side(0)    [T2 - 1]
    wrap()

# Create the state machine
sm = rp2.StateMachine(0, ws2812, freq=8000000, sideset_base=machine.Pin(PIN_NUM))

# Start the state machine
sm.active(1)

# Function to convert RGB values to a 24-bit color
def rgb_to_color(r, g, b):
    return (r << 16) | (g << 8) | b

# Function to show colors on the Neopixel strip
def show(colors):
    dimmed_colors = array.array("I", [0] * NUM_LEDS)
    for i, color in enumerate(colors):
        r = int((color >> 16) & 0xff * brightness)
        g = int((color >> 8) & 0xff * brightness)
        b = int(color & 0xff * brightness)
        dimmed_colors[i] = (r << 16) | (g << 8) | b
    sm.put(dimmed_colors, 8)

# Cycle through different colors
while True:
    colors = [rgb_to_color(255, 0, 0)] * NUM_LEDS  # Red
    show(colors)
    time.sleep(1)
    
    colors = [rgb_to_color(0, 255, 0)] * NUM_LEDS  # Green
    show(colors)
    time.sleep(1)
    
    colors = [rgb_to_color(0, 0, 255)] * NUM_LEDS  # Blue
    show(colors)
    time.sleep(1)
    
    colors = [rgb_to_color(255, 255, 0)] * NUM_LEDS  # Yellow
    show(colors)
    time.sleep(1)
    
    colors = [rgb_to_color(0, 255, 255)] * NUM_LEDS  # Cyan
    show(colors)
    time.sleep(1)
    
    colors = [rgb_to_color(255, 0, 255)] * NUM_LEDS  # Magenta
    show(colors)
    time.sleep(1)
