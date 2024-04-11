import time

# leds
def stim0(pin):
    pin.off()

def stim1(pin):
    pin.on()

# servo
def stim2(servo, reps=5):
    servo.ServoAngle(90)
    time.sleep(0.5)

    for i in range(reps):
        servo.ServoAngle(110)
        time.sleep(0.1)
        servo.ServoAngle(70)
        time.sleep(0.1)


    time.sleep(0.5)
    servo.ServoAngle(0)


def stim3(servo, reps=5):
    servo.ServoAngle(90)
    time.sleep(0.5)

    for i in range(reps):
        servo.ServoAngle(70)
        time.sleep(0.1)
        servo.ServoAngle(110)
        time.sleep(0.1)

    time.sleep(0.5)
    servo.ServoAngle(0)
