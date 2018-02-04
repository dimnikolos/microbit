#buzzer
#show the fastest of two players
from microbit import *

display.scroll('Buzzer', wait = True)

while True:
    if button_a.is_pressed():
        display.show('A')
        sleep(5000)
    if button_b.is_pressed():
        display.show('B')
        sleep(5000)
    display.show(Image.ASLEEP)
