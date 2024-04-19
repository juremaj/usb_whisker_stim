import time
import random

def stim0(dir, pul, n_steps=1600, isi=0.0009):
    dir.value(0) # direction of spin (only difference between stimuli)

    for i in range(n_steps):
        pul.value(1)
        time.sleep(isi)
        pul.value(0)
        time.sleep(isi)

def stim1(dir, pul, n_steps=1600, isi=0.0009):
    dir.value(1) # direction of spin (only difference between stimuli)

    for i in range(n_steps):
        pul.value(1)
        time.sleep(isi)
        pul.value(0)
        time.sleep(isi)
    
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
            count = 0

        count+=1

        pul.value(1)
        time.sleep(isi)
        pul.value(0)
        time.sleep(isi)