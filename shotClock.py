#shotClock
#A basketball shot clock
#Button A: Stops timer
#Button B: Resets timer
from microbit import *

display.scroll('Shot Clock')

def getImage(num):
    num2images = {
        0:  '09900:90090:90090:90090:09900',
        1:  '00900:09900:00900:00900:09990',
        2:  '99900:00090:09900:90000:99990',
        3:  '99990:00090:00900:90090:09900',
        4:  '00990:09090:90090:99999:00090',
        5:  '99999:90000:99990:00009:99990',
        6:  '00090:00900:09990:90009:09990',
        7:  '99999:00090:00900:09000:90000',
        8:  '09990:90009:09990:90009:09990',
        9:  '09990:90009:09990:00900:09000',
        10: '90999:90909:90909:90909:90999',
        11: '90090:90090:90090:90090:90090',
        12: '90999:90009:90999:90900:90999',
        13: '90999:90009:90999:90009:90999',
        14: '90909:90909:90999:90009:90009',
        15: '90999:90900:90999:90009:90999',
        16: '90999:90900:90999:90909:90999',
        17: '90999:90009:90009:90009:90009',
        18: '90999:90909:90999:90909:90999',
        19: '90999:90909:90999:90009:90999',
        20: '99999:09909:99909:90909:99999',
        21: '99090:09090:99090:90090:99090',
        22: '99099:09009:99099:90090:99099',
        23: '99099:09009:99099:90009:99099',
        24: '99909:09909:99999:90009:99009'}

    if num < 0 or num > 24:
        display.show(Image.SAD)
        return(None)
    return(Image(num2images[num]))


counter = 25
running = True
startRunningTime = running_time()
while(True):
    if running_time() - startRunningTime > 1000 and running:
        startRunningTime = running_time()
        if counter > 0:
            counter -= 1
            display.show(getImage(counter))
        else:
            display.show(Image.SAD)
            running = False
    if button_a.was_pressed():
        if running:
            running = False
        else:
            running = True
            startRunningTime = running_time()
    if button_b.was_pressed():
        counter = 25
        running = True
        startRunningTime = running_time()

