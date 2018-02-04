#quotes
#Button A shows a movie quote
#Button B shows the title of the corresponding movie
from microbit import *
import random

display.scroll('Quotes', wait = True)

movies = {"Why so serious?":"The Dark Knight, 2008",
    "Hello. My name is Inigo Montoya. You killed my father. Prepare to die.":"The Princess Bride, 1987",
    "I am your father.":"Star Wars Episode V: The Empire Strikes Back, 1980",
    "The first rule of Fight Club is: You do not talk about Fight Club.":"Fight Club, 1999",
    "There's no place like home.":"The Wizard of Oz, 1939",
    "You talkin' to me?":"Taxi Driver, 1976",
    "Of all the gin joints in all the towns in all the world, she walks into mine.":"Casablanca, 1942",
    "I'm going to make him an offer he can't refuse.":"The Godfather, 1972",
    "Toto, I've a feeling we're not in Kansas anymore.":"The Wizard of Oz, 1939",
    "May the Force be with you.":"Star Wars, 1977",
    "You're gonna need a bigger boat.":"Jaws, 1975",
    "Here's looking at you, kid.":"Casablanca, 1942",
    "Frankly, my dear, I don't give a damn.":"Gone With the Wind, 1939"}
    
showedAnswer = False
randomQuote = random.choice(list(movies.keys()))
while True:
    if button_a.was_pressed():
        if showedAnswer:
            randomQuote = random.choice(list(movies.keys()))
            showedAnswer = False
            display.scroll(randomQuote, wait = False)
        else:
             display.scroll(randomQuote, wait = False)
    if button_b.was_pressed():
        if randomQuote:
            display.scroll(movies[randomQuote], wait = False)
            movies.pop(randomQuote)
            showedAnswer = True

