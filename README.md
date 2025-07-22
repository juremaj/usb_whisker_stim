# usb_whisker_stim
Simple USB device for whisker stimulation

## Dependencies

You need to install pyserial on the host pc to communicate with the Pico. The demo `trigger_stim.py` script also uses numpy.
```
pip install pyserial
pip install numpy
```

## Hardware
- For instruction on how to wire up the device see the pictures in `resources/pics_stepper`
- This involves three simple steps:
    1) connecting 4 motor pins to the motor driver
    2) connecting +/- of 12 V power adapter to motor driver
    3) connecting 4 pico pins to the motor driver
- Then the final step is to configure the stepper settings (current and number of steps per revolution) - see the table on the driver and driver_settings.png for the default setting (DOWN DOWN DOWN DOWN DOWN UP DOWN)
- The 3d printed parts are optional, mostly as adapters (for example to screw the parts into a thorlabs optics breadboard and to relay the rotation of the stepper to a rod for whisker stim) - but these can easily be replaced by other parts

## Raspberry Pico code
- All code to be uploaded to raspberry pico is available in `pico_usb_whisker_stim`.
- To see how to put the code to the raspberry pico you can follow the steps here: https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/5 
- Most important steps:
    - Set up a way to control the pico from your computer (Thonny IDE in this case)
    - Add micropython firmware to the board
    - Test if everything works ('blink' onboard LED)
    - Check the intructions on how to upload a script
    - The only thing that needs to be uploaded is the `usb_whisker_stim/main.py` script

## Demo
- Once you have followed the instructions above you can test if the motor works
- The code `trigger_stim.py` is an example of how the device can be used to randomly deliver one of the 2 pre-programmed stimuli
- The only thing that needs to be changed is line 7 to tell the script where it can find the pico (this will depend on the OS and to which port the pico gets connected)
- This would usually be done by another script running the experimental protocol (for example the camera synchronisation scripts in `control_exp`)

## 'backup' folders
These contain older version of code and resources (mostly for a version using a servo instead of stepper motor) - these should be ignored.