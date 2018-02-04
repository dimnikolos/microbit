#quotes2
#Button A shows a movie quote
#Button B shows the title of the corresponding movie
#needs quotes.txt
#How to use:
#pip install microfs
#flash microbit with code
#ufs put ./quotes.txt
#reset microbit

from microbit import *
import random


def readFromFile(line):
    with open('quotes.txt','r') as f:
            for _ in range(line-1):
                f.readline()
            themovie = f.readline()
            return(themovie.split(':'))

listi = list(range(0,99))
movnum = listi.pop(random.randint(0,len(listi)-1))
movie = readFromFile(movnum)
showedAnswer = False
while True:
    if button_a.was_pressed():
        if showedAnswer:
            movnum = listi.pop(random.randint(0,len(listi)-1))
            movie = readFromFile(movnum)
            display.scroll(movie[0], wait = False)
        else:
            display.scroll(movie[0], wait = False)
    if button_b.was_pressed():
        display.scroll(movie[1], wait = False)
        showedAnswer = True
        