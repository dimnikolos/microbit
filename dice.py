from microbit import *
import random
def getDiceImage(num):
    num2images = {
        1: '00000:00000:00900:00000:00000',
        2: '00000:09000:00000:00090:00000',
        3: '90000:00000:00900:00000:00009',
        4: '00000:09090:00000:09090:00000',
        5: '90009:00000:00900:00000:90009',
        6: '09090:00000:09090:00000:09090'}
    if num < 1 or num > 6:
        display.show(Image.SAD)
        return(None)
    return(Image(num2images[num]))
 
while True:
    if button_a.was_pressed():
        display.clear()
        sleep(500)
        display.show(getDiceImage(random.randrange(1,6)))
        