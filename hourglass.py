#hourglass
#Shows a hourglass for a specific time
from microbit import *

display.scroll('Hourglass', wait = True)

hourglassImages = [
    '99999:99999:99999:99999:99999',
    '00000:99999:99999:99999:99999',
    '00000:00000:99999:99999:99999',
    '00000:00000:00000:99999:99999',
    '00000:00000:00000:00000:99999',
    '00000:00000:00000:00000:00000']

def runTimer(t):
    """t is timer time in milliseconds"""
    blinkrow = 500 #in milliseconds
    eachrow = t // 5 
    for i in range(5):
        for _ in range(eachrow//(2*blinkrow)):
            display.show(Image(hourglassImages[i+1]))
            sleep(blinkrow)
            display.show(Image(hourglassImages[i]))
            sleep(blinkrow)
            if button_b.was_pressed():
                return()
    display.show(Image.HAPPY)
    return()
while True:
    if button_a.was_pressed():
        runTimer(20000)#runTimer for 20 seconds
