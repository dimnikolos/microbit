#xmas
#A christmas tree animation
from microbit import *
import random

display.scroll('Xmas', wait = True)

def makeImageFromLeds(arr):
    try:
        retim =  "00"+str(arr[0]) + "00:"
        retim += "0"+str(arr[1])+"3"+str(arr[2])+"0:"
        retim += "00300:"
        retim += str(arr[3])+str(arr[4])+"3"+str(arr[5])+str(arr[6])+":"
        retim += "00300"
        print(retim)
        return(retim)
    except IndexError:
        display.show(Image.SAD)
        
while(True):
    display.show(Image(makeImageFromLeds([random.randint(0,9) for _ in range(7)])))
    sleep(random.randint(1,4)*500)

