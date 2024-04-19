import sys
from stim import stim0, stim1, stim2

from machine import Pin
import time

import random

def stim2(dir, pul, n_steps=16000, n_steps_change=1000, isi=0.0009):

    # change direction after random number of steps:
    print("new stim2")
    # randomly choose n_steps_change to be between 10 and 100
    n_steps_change = random.randint(10, 100)

    count = 0 
    for i in range(n_steps):
        # randomly choose duration of this step between 0.01 and 0.001

        # randomly sample direction every n_steps_change steps
        if count == n_steps_change:
            print("nwwww")
            dir.value(random.choice([0, 1]))
            isi = random.uniform(0.001, 0.01)
            # multiply n_steps_change by 1 if its close to 0.01 and by 10 if it is close to 0.001
            n_steps_change = random.randint(10, int(1/isi))
            count = 0

        count+=1

        pul.value(1)
        time.sleep(isi)
        pul.value(0)
        time.sleep(isi)


n_steps = 1600 # number of steps (set depending on hardware setting)
isi = 0.0009 # how fast to rotate 

# blink led to shwo connection
pin = Pin("LED", Pin.OUT)

# blink three times to show it is connected
for i in range(6):
    pin.toggle()
    time.sleep(0.2)

# define pins to interface with the stepper motor driver
pul = Pin(12, Pin.OUT)
dir = Pin(13, Pin.OUT)
opto = Pin(14, Pin.OUT)
ena = Pin(15, Pin.OUT)

pul.value(0)# initialize the pulse and direction pins to low
dir.value(0) # -II-
ena.value(1) # dont yet enable the motor driver
opto.value(1) # set opto to up (this should be 3.3V reference, see answer here: https://stackoverflow.com/questions/62056411/stepper-motor-control-with-dm320t-raspberry-pi-3b-and-matlab)

time.sleep(1)

# now wait for the command to trigger the stim
# (the command arrives via usb serial)

while True:
    try:
        command = sys.stdin.readline().strip()
        
        print(f"Triggering stim: {command}")

        if command.lower() == "0":
            stim0(dir, pul, n_steps=n_steps, isi=isi)

        elif command.lower() == "1":
            stim1(dir, pul, n_steps=n_steps, isi=isi)
        
        elif command.lower() == "2":
            stim2(dir, pul, n_steps=160000, n_steps_change=100, isi=0.001)

        else:
            # quick blink if command not recognized
            for i in range(10):
                pin.toggle()
                time.sleep(0.1)

    except KeyboardInterrupt:

        pul.value(0)
        dir.value(0)
        opto.value(0)
        ena.value(0)

        break

# disable the driver
pul.value(0)
dir.value(0)
opto.value(0)
ena.value(0)


