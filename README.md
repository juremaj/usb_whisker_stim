# usb_whisker_stim
Simple USB device for whisker stimulation

## Dependencies

You need to install pyserial on the host pc to communicate with the Pico. The demo `trigger_stim.py` script also uses numpy.
```
pip install pyserial
pip install numpy
```

## Raspberry Pico code
- All code to be uploaded to raspberry pico is available in `pico_whisker_stim`.
- Before transferring the files make sure that MicroPython is flashed onto the board.
- A conventient way to deal with this (also easiest to debug) is to use VSCode with the MicroPico extension (this allows a simple initiation and upload of pico project via USB)


## Hardware
- Instructions for all hardware (electronics and 3d printed) are available in `resources`


## Simple use case
- The code `trigger_stim.py` is an example of how the device can be used to randomly deliver one of the 2 pre-programmed stimuli
- This would usually be done by another script running the experimental protocol (for example the camera synchronisation scripts in `control_exp`)
