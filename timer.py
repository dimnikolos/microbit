#stopwatch
#a starts and stops watch
#b displays all recorded times
#and resets
from microbit import *

strtTime = 0
stopped = []    
while True:
    if button_a.was_pressed():
        if not strtTime == 0:
            rt = running_time()
            secs = (rt-strtTime) // 1000
            secs100 = (rt - strtTime - secs* 1000)//100
            display.scroll(str(secs)+'.'+str(secs100), wait = False, loop = True)
            stopped.append(str(secs)+'.'+str(secs100))
        else:
            strtTime = running_time()
            display.show('0')
    if button_b.was_pressed():
        display.scroll(','.join(stopped), wait = False)
        stopped = []
        strtTime = 0
        