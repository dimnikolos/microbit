# With just a microbit

Projects that use only a single microbit and nothing else.

## Getting Started

You need a single microbit. And the [Mu Editor](https://codewith.mu/), just hit 
Flash (except for quotes2.py, see below) and go.

##Projects
* bingo.py: A random bingo ball appears on the led screen (button A). With button B you can see all
the balls that have been drawn from the pool.

* buzzer.py: Who is faster button A player or button B player?

* counter.py: Counts number of times button A is pressed, microbit remembers even if it is powered off.

* dice.py: Throw two dices.

* die.py: Throw a dice with images.

* hourglass.py: A hourglass timer.

* pickacard.py: Picks a random card from a deck.

* pickaLetter.py: Picks a letter from the alphabet as if it is fastly recited.

* quotes.py: Button A shows a movie quote. Button B shows the title of the movie. Can you find the 
movie without pressing button B?

* quotes2.py: Same as the previous one but uses quotes.txt.
Step 1: Flash the microbit with the code

Step 2:
```
ufs put ./quotes.txt
```
To put the file on the microbit. If you don't have the ufs command then you have to run
```
pip install microfs
```
first.

Step 3:
Reset your microbit (back button).

* reflex.py: Measures reflexes for button A and button B.

* shotClock.py: A basketball shot clock (24 seconds). Button A starts and stops timer, button B resets.

* teetotum.py: A teetotum where six messages appear.

* timer.py: A stopwatch timer. Button A starts/stops timer, button B shows the measures times and resets.

* xmas.py: A christmas tree animation.

## Built With

* [Mu Editor](https://codewith.mu/)

## Authors

* **Dimitris Nikolos** - [github](https://github.com/dimnikolos), [twitter](https://twitter.com/dnikolos)

## Acknowledgments

* Inspiration from [martinohanlon](https://github.com/martinohanlon/microbit-micropython)

