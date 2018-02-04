#pythagorean
#button A asks a multiplication question
#button B shows the answer
from microbit import *
import random

display.scroll('Pythagorean test')
i = 0
j = 0
while True:
    if button_a.was_pressed():
        i = random.randint(1,9)
        j = random.randint(1,9)
        s = str(i) + 'x' + str(j) + '=?'
        display.scroll(s, wait = False, loop = True)
    if button_b.was_pressed():
        display.scroll(str(i*j))
