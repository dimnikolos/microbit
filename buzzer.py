#buzzer
from microbit import *
while True:
    if button_a.is_pressed():
        display.show('A')
        sleep(5000)
    if button_b.is_pressed():
        display.show('B')
        sleep(5000)
    display.show(Image.ASLEEP)