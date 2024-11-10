from machine import Pin
import time

pul = Pin(12, Pin.OUT)
dir = Pin(13, Pin.OUT)
opto = Pin(14, Pin.OUT)
ena = Pin(15, Pin.OUT)

n_steps = 400
isi = 0.0009

pul.value(0)
dir.value(0)
opto.value(0)
ena.value(0)

time.sleep(1)

# enable the driver
ena.value(1)
# set opto (this should be 3.3V reference, see answer here: https://stackoverflow.com/questions/62056411/stepper-motor-control-with-dm320t-raspberry-pi-3b-and-matlab)
opto.value(1)

time.sleep(1)

# pulse the stepper motor
for i in range(n_steps):
    pul.value(1)
    time.sleep(isi)
    pul.value(0)
    time.sleep(isi)

# change direction
dir.value(1)

time.sleep(1)

# repeat
for i in range(n_steps):
    pul.value(1)
    time.sleep(isi)
    pul.value(0)
    time.sleep(isi)


time.sleep(1)

# disable the driver
pul.value(0)
dir.value(0)
opto.value(0)
ena.value(0)