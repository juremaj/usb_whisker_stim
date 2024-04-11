# first testing the pins if they work or not

from machine import Pin
import time

# define the pins 12, 13, 14, 15
p12 = Pin(12, Pin.OUT)
p13 = Pin(13, Pin.OUT)
p14 = Pin(14, Pin.OUT)
p15 = Pin(15, Pin.OUT)

# blink the pins
for i in range(10):
    p12.value(1)
    time.sleep(0.5)
    p12.value(0)
    time.sleep(0.5)

    p13.value(1)
    time.sleep(0.5)
    p13.value(0)
    time.sleep(0.5)

    p14.value(1)
    time.sleep(0.5)
    p14.value(0)
    time.sleep(0.5)

    p15.value(1)
    time.sleep(0.5)
    p15.value(0)
    time.sleep(0.5)
