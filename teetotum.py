#teetotum
#Shows random images of
#Take 1
#Put 1
#Put 2
#All Put
#Take All
from microbit import *
import random

display.scroll('Teetotum', wait = True)
msgs = ['T1','P2','P1','AP','TA']
while True:
    if button_a.was_pressed():
        display.clear()
        sleep(500)
        display.scroll(random.choice(msgs), loop = True, wait = False)

