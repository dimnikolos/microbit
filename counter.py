#counter
#counts button_a presses
#b resets
from microbit import *

display.scroll("Counter", wait = True)

try:
    with open('counts.txt','r') as f:
        count = int(f.readline())
except OSError:
    count = 0

while True:
    if button_a.was_pressed():
        count += 1
        with open('counts.txt','w') as f:
            f.write(str(count))
        display.scroll(str(count),wait = False)
    if button_b.was_pressed():
        count = 0
        with open('counts.txt','w') as f:
            f.write(str(count))
        display.scroll(str(count),wait = False)

