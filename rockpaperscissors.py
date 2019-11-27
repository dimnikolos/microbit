from microbit import *
from random import *

rock  = Image('00000:09990:99999:09990:00000')
paper = Image('00999:09999:99999:99999:99999')
scissor = Image('90099:09099:00900:09099:90099')
empty = Image('00000:00000:00000:00000:00000')
rpsIm = [rock,paper,scissor]
while (True):
    while (True):
      if (button_a.was_pressed()):
        break
    randomA = randint(0,2)
    display.show(rpsIm[randomA])
    while (True):
      if (button_b.was_pressed()):
        break
    display.clear()
    sleep(500)
    randomB = randint(0,2)
    display.show(rpsIm[randomB])
    sleep(3000)
    if (randomA-randomB)%3 == 0:
      display.scroll('Tie')
    elif (randomA-randomB)%3 == 1:
      display.scroll('A wins')
    elif (randomA-randomB)%3 == 2:
      display.scroll('B wins')
    sleep(1000)
    
    
