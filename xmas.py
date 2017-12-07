from microbit import *
import random

def makeImageFromLeds(arr):
    try:
        retim =  "00"+str(arr[0]) + "00:"
        retim += "0"+str(arr[1])+"9"+str(arr[2])+"0:"
        retim += "00900:"
        retim += str(arr[3])+str(arr[4])+"9"+str(arr[5])+str(arr[6])+":"
        retim += "00900"
        print(retim)
        return(retim)
    except IndexError:
        display.show(Image.SAD)
        
while(True):
    display.show(Image(makeImageFromLeds([random.randint(0,9) for _ in range(7)])))
    sleep(random.randint(1,4)*500)
    
