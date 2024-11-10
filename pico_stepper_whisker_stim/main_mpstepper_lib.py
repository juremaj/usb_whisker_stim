
from MpStepper import Stepper
import time

stepper = Stepper(12, 13, steps_per_rev=1600, speed_sps=1600)
print('test')
print(stepper.get_pos_deg())
# stepper.enable(0)
time.sleep(1)
stepper.target_deg(90)
print(stepper.get_pos_deg())
time.sleep(1)
stepper.target_deg(0)








# n_steps = 1600 # number of steps (set depending on hardware setting)
# isi = 0.0009 # how fast to rotate 

# # blink led to shwo connection
# pin = Pin("LED", Pin.OUT)

# # blink three times to show it is connected
# for i in range(6):
#     pin.toggle()
#     time.sleep(0.2)

# # define pins to interface with the stepper motor driver
# pul = Pin(12, Pin.OUT)
# dir = Pin(13, Pin.OUT)
# opto = Pin(14, Pin.OUT)
# ena = Pin(15, Pin.OUT)

# pul.value(0)# initialize the pulse and direction pins to low
# dir.value(0) # -II-
# ena.value(0) # dont yet enable the motor driver
# opto.value(1) # set opto to up (this should be 3.3V reference, see answer here: https://stackoverflow.com/questions/62056411/stepper-motor-control-with-dm320t-raspberry-pi-3b-and-matlab)

# time.sleep(1)

# # now wait for the command to trigger the stim
# # (the command arrives via usb serial)

# while True:
#     try:
#         command = sys.stdin.readline().strip()
        
#         print(f"Triggering stim: {command}")

#         if command.lower() == "0":
#             ena.value(1)
#             time.sleep(1)
#             stim0(dir, pul, n_steps, isi)
#             print('TAC')
#             ena.value(0)
#             time.sleep(2)
#             ena.value(1)
#             time.sleep(1)
#             stim0(dir, pul, n_steps, isi)
#             ena.value(0)
#             time.sleep(2)


#         elif command.lower() == "1":
#             stim1(dir, pul, n_steps=n_steps, isi=isi)
        
#         elif command.lower() == "2":
#             stim2(dir, pul, n_steps=160000, n_steps_change=100, isi=0.001)

#         else:
#             # quick blink if command not recognized
#             for i in range(10):
#                 pin.toggle()
#                 time.sleep(0.1)

#     except KeyboardInterrupt:

#         pul.value(0)
#         dir.value(0)
#         opto.value(0)
#         ena.value(1)

#         break

# # disable the driver
# pul.value(0)
# dir.value(0)
# opto.value(0)
# ena.value(0)


