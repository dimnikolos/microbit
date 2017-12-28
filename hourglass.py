#hourglass
from microbit import *
hourglassImages = [
    '99999:99999:99999:99999:99999',
    '00000:99999:99999:99999:99999',
    '00000:00000:99999:99999:99999',
    '00000:00000:00000:99999:99999',
    '00000:00000:00000:00000:99999',
    '00000:00000:00000:00000:00000']
t = 15 #in seconds
wholeAnimation = t * 1000 # in ms
eachrow = wholeAnimation // 5
blinkrow = eachrow // 20
while True:
    if button_a.was_pressed():
        display.show(Image.SAD)
        for i in range(5):
            for _ in range(10):
                display.show(Image(hourglassImages[i+1]))
                sleep(blinkrow)
                display.show(Image(hourglassImages[i]))
                sleep(blinkrow)
                
        display.clear()
