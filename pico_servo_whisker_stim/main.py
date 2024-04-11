# flash led on raspberry pico

from machine import Pin
from utime import sleep
import time
import sys
from servo import Servo
from stim import stim0, stim1, stim2, stim3


servo = Servo(16)
servo.ServoAngle(0)

pin = Pin("LED", Pin.OUT)

# blink three times to show it is connected
for i in range(6):
    pin.toggle()
    sleep(0.2)


while True:
    # blink three times when connected 
    try:
        servo.ServoAngle(0) # init position

        command = sys.stdin.readline().strip()
        print(f"Triggering stim: {command}")
        
        if command.lower() == "0":
            stim0(pin)
            stim2(servo)

        elif command.lower() == "1":
            stim1(pin)
            stim3(servo)

        else:
            # quick blink if command not recognized
            for i in range(10):
                pin.toggle()
                sleep(0.1)

        
    except KeyboardInterrupt:
        servo.deinit()
        break

pin.off()
print("Finished.")