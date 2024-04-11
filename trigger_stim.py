import serial
import time
import numpy as np

# Open serial port
ser = serial.Serial('/dev/cu.usbmodem1101', 9600) # IMPORTANT: for some reason the port is cu vs tty
# clear buffer
ser.reset_input_buffer()
ser.reset_output_buffer()

# generate random string of zeros and ones
stim_protocol = [stim for stim in np.random.randint(0,2,100)]
print('stim_protocol: ', stim_protocol)

for stim in stim_protocol:
    try:
        print('input: ', stim)
        stim_towrite = str(stim) + '\n'
        ser.write(stim_towrite.encode('utf-8'))
        rep = ser.readline()
        print('output: ', rep.decode('utf-8'))

        # wait 10 seconds between stimulations
        time.sleep(10)
    except KeyboardInterrupt:
        break

ser.close()
print('done')
