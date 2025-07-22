import sys

from machine import Pin
import utime
import time


def stim0(dir, pul, n_steps_pos=1600, n_steps_stim = 400, n_stim_rep=4, isi=0.0009):
    dir.value(1) # direction of spin (only difference between stimuli)

    for i in range(n_steps_pos):
        pul.value(1)
        utime.sleep_us(isi)
        pul.value(0)
        utime.sleep_us(isi)

    # start measuring time
    start_time = utime.ticks_ms()
    for i in range(n_stim_rep*2):
        dir.value((i+1) % 2)  # alternate direction for each repetition
        for j in range(n_steps_stim):
            pul.value(1)
            utime.sleep_us(isi)
            pul.value(0)
            utime.sleep_us(isi)
    end_time = utime.ticks_ms()
    elapsed_time = utime.ticks_diff(end_time, start_time)
    print(f"Elapsed time for stimulus: {elapsed_time} ms")
    dir.value(0)

    for i in range(n_steps_pos):
        pul.value(1)
        utime.sleep_us(isi)
        pul.value(0)
        utime.sleep_us(isi)

# n_steps = 1600 # number of steps (set depending on hardware setting)
n_steps_pos = 300
n_steps_stim = 500 # 500 # number of steps for the stimulus
n_stim_rep = 5 # number of repetitions of the stimulus
isi = 185 # 185 # how fast to rotate

# blink led to show connection
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
ena.value(0) # dont yet enable the motor driver
opto.value(1) # set opto to up (this should be 3.3V reference, see answer here: https://stackoverflow.com/questions/62056411/stepper-motor-control-with-dm320t-raspberry-pi-3b-and-matlab)

time.sleep(1)

# now wait for the command to trigger the stim
# (the command arrives via usb serial)

while True:
    ena.value(1)
    try:
        command = sys.stdin.readline().strip()
        
        print(f"Triggering stim: {command}")
        
        if command.lower() == "0":
            # stim0(dir, pul, n_steps, isi)
            stim0(dir, pul, n_steps_pos=n_steps_pos, n_steps_stim=n_steps_stim, n_stim_rep=n_stim_rep, isi=isi)
            print('TAC')


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


