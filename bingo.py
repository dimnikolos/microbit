#bingo
#select and remove a random bingo ball
from microbit import *
import random

display.scroll('Bingo', wait = True)

num = 90 #or 75
balls = list(range(1,num))
drawn = []
while True:
    if button_a.was_pressed():
        if len(balls) == 0:
            display.show(Image.HAPPY)
        else:
            randomBallIndex = random.randint(0,len(balls)-1)
            randomBall = balls.pop(randomBallIndex)
            drawn.append(randomBall)
            display.scroll(str(randomBall),loop = True, wait = False)
    if button_b.was_pressed():
        display.scroll(','.join([str(b) for b in drawn]), wait = False, loop = True)

