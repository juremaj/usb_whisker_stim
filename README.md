# usb_whisker_stim
Simple USB device for whisker stimulation

## Hardware
### Components list:
- [Raspberry Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/) 
- [Motor](https://www.omc-stepperonline.com/fr/nema-8-bipolaire-1-8deg-4ncm-5-7oz-in-0-6a-6v-20x20x38mm-4-fils-8hs15-0604s?srsltid=AfmBOopk5yiqgoLouQ6k0vKjGUFTYhUCFirBDUTsyYDL8u_syfw4GUZw) (Nema 8 Bipolar 1.8deg 4Ncm(5.7oz.in) 0.6A 20x20x38mm 4 Wires model: 8HS15-0604S)
- [Driver](https://www.omc-stepperonline.com/fr/pilote-numerique-pas-a-pas-0-3-2-2a-10-30vdc-pour-nema-8-11-14-16-17-moteur-pas-a-pas-dm320t?srsltid=AfmBOor4CZzB0a09o4nP59VcgGCvBjCYBjOBE6GV5xBhgGucQqpYNq2G) (Digital Stepper Driver 0.3-2.2A 10-30VDC for Nema 8, 11, 14, 16, 17 Stepper Motor, model: DM320T)
- Articulated arm

### Setup:
- For instruction on how to wire up the device see the pictures in `resources/pics_stepper`
- This involves three simple steps:
    1) connecting 4 motor pins to the motor driver
    2) connecting +/- of 12 V power adapter to motor driver
    3) connecting 4 pico pins to the motor driver
- Then the final step is to configure the stepper settings (current and number of steps per revolution) - see the table on the driver and `driver_settings.png` for the default setting (DOWN DOWN DOWN DOWN DOWN UP DOWN)

## Raspberry Pico code
- All code to be uploaded to raspberry pico is available in `pico_whisker_stim`.
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
- To run that code you will need to `pip install pyserial` and `pip install numpy` - ideally in a virtual environment such as conda
- The only thing that needs to be changed is line 7 to tell the script where it can find the pico (this will depend on the OS and to which port the pico gets connected) 
- This would usually be done by another script running the experimental protocol (for example the camera synchronisation scripts in `control_exp`)

## 3D printing

- The 3d printed parts are optional, mostly as adapters (for example to screw the parts into a thorlabs optics breadboard and to relay the rotation of the stepper to a rod for whisker stim) - but these can easily be replaced by other parts
- All parts are available in `resources/3dprint_stepper` and under `resources/links.md` there is also a link to an external case also available here: [Raspberry Pico Case](https://www.thingiverse.com/thing:4737733)


## 'backup' folders
These contain older version of code and resources - these can be ignored.
