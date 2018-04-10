from microbit import *
from random import random

"""
Answer to cassidoo interview question for 4.2.2018: 
Given a matrix of 0s and 1s, where 0s are bodies of water and 1s are bodies of land, 
return the number of land masses. Land is connected horizontally and/or vertically. 
"""
def list2img(l):
    s = ':'.join([''.join([str(x) for x in row]) for row in l])
    return(Image(s))


def randlist():
    li = []
    for _ in range(5):
        li.append([])
        for _ in range(5):
            li[-1].append(9*round(random()))
    return(li)


def propagateLand(l, lid):
    """
    l is the list
    lid is the land id
    """
    changed = True
    while changed:
        changed = False
        for (x, row) in enumerate(l):
            for (y, elem) in enumerate(row):
                if l[x][y] == 9:
                    for d in [-1, 1]:
                        if 0 <= x+d < 5 and l[x+d][y] == lid:
                            l[x][y] = lid
                            changed = True
                        if 0 <= y+d < 5 and l[x][y+d] == lid:
                            l[x][y] = lid
                            changed = True


def findLands(l):
    lands = 0
    landid = 9
    for (x, row) in enumerate(l):
        for (y, elem) in enumerate(row):
            if elem == 9:
                lands += 1
                landid -= 1
                l[x][y] = landid
                propagateLand(l, landid)
                display.show(list2img(l))
                sleep(1000)
    return(lands)


while True:
    rli = randlist()
    display.show(list2img(rli))
    sleep(1000)
    lands = findLands(rli)
    display.show(str(lands))
    sleep(1000)
