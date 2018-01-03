#reflex
#Displays A or B and
#the time in which the player presses
#the corresponding time
from microbit import *
import random

display.scroll('Reflex', wait = True)

buttons = ['A','B']
while True:
    sleep(random.randint(2000,3000))
    button = random.choice(buttons)
    display.show(button)
    strt = running_time()
    if button == 'A':
        while not button_a.is_pressed():
            pass
        reflex = running_time() - strt
        display.scroll(str(reflex),wait = True)
    elif button == 'B':
        while not button_b.is_pressed():
            pass
        reflex = running_time() - strt
        display.scroll(str(reflex),wait = True)
        
    