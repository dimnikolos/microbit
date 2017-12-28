#pick a card
from microbit import *
import random
ImageSPADE = Image('00900:09990:99999:90909:00900')
ImageCLUB = Image('09990:09990:99099:99099:00900')

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

suitsImages = {
    'hearts':Image.HEART, 
    'diamonds':Image.DIAMOND, 
    'spades':ImageSPADE, 
    'clubs':ImageCLUB}
    
suits = ['hearts', 'diamonds', 'spades', 'clubs']
values = ['2','3','4','5','6','7','8','9','A','J','Q','K']
deck = [Card(value, suit) for value in values for suit in suits]

randomCard = random.choice(deck)
while True:
    if button_a.was_pressed():
        display.clear()
        sleep(500)
        randomCard = random.choice(deck)
    display.show(randomCard.value)
    sleep(500)
    display.show(suitsImages[randomCard.suit])
    sleep(500)
        