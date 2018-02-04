#pickaLetter
#button A starts the alphabet
#button B stops the alphabet and 
#shows the chosen letter.
from microbit import *

display.scroll('Pick a letter')

letter = ['A','B','C','D','E','F','G','H','I','J',
            'K','L','M','N','O','P','Q','R','S','T',
            'U','V','W','X','Y','Z']
while True:
    if button_a.is_pressed():
        display.show('A')
        sleep(1000)
        strt = running_time()
        display.show(Image.ALL_CLOCKS, wait=False, loop = True)
    if button_b.is_pressed():
        display.show(letter[((running_time()-strt)//200)%26])

