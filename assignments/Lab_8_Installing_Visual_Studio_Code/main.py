
### main.py

import machine
import utime

led = machine.Pin(25, machine.Pin.OUT)

while True:
    led.value(1)
    utime.sleep(1)
    led.value(0)
    utime.sleep(1)
