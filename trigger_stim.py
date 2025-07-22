import serial
import time
import numpy as np


# 1) Open serial port

# IMPORTANT: this needs to be changed depending on your system and which port the pico is connected to

ser = serial.Serial('/dev/tty.usbmodem1401', 9600)

ser.reset_input_buffer()
ser.reset_output_buffer()


# 2) Generate random string of zeros and ones

# if using the default main.py:
#       - when stim is 0 the motor will be triggered and 
#       - when it is 1 the motor will not be triggered

# if using the main_two_stimuli.py:
#       - when stim is 0 the motor will be triggered in one direction
#       - when it is 1 the motor will be triggered in the other direction

stim_protocol = [stim for stim in np.random.randint(0,2,100)]
print('stim_protocol: ', stim_protocol)


# 3) Run the stimulation protocol

for stim in stim_protocol:
    try:
        print('input: ', stim)
        stim_towrite = str(stim) + '\n'
        ser.write(stim_towrite.encode('utf-8'))
        rep = ser.readline()
        print('output: ', rep.decode('utf-8'))

        # wait 3 seconds between stimulations
        time.sleep(3)
    except KeyboardInterrupt:
        break

ser.close()
print('done')
