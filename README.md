# With just a microbit

Projects that use only a single microbit and nothing else.

## Getting Started

You need a single microbit. And the [Mu Editor](https://codewith.mu/), just hit 
Flash (except for quotes2.py, see below) and go.

## Projects
1. bingo.py: A random bingo ball appears on the led screen (button A). With button B you can see all
the balls that have been drawn from the pool.

2. buzzer.py: Who is faster button A player or button B player?

3. counter.py: Counts number of times button A is pressed, microbit remembers even if it is powered off.

4. dice.py: Throw two dice (using images).

5. die.py: Throw a die (using images).

6. hourglass.py: A hourglass timer.

7. pickacard.py: Picks a random card from a deck.

8. pickaLetter.py: Picks a letter from the alphabet as if it is fastly recited.

9. pythagorean.py: A Pythagorean table quiz. Button A asks questions and button B shows correct answer.

10. quotes.py: Button A shows a movie quote. Button B shows the title of the movie. Can you find the 
movie without pressing button B?

11. quotes2.py: Same as the previous one but uses quotes.txt.

	Step 1: Flash the microbit with the code.

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

12. reflex.py: Measures reflexes for button A and button B.

13. shotClock.py: A basketball shot clock (24 seconds). Button A starts and stops timer, button B resets.

14. teetotum.py: A teetotum where six messages appear.

15. timer.py: A stopwatch timer. Button A starts/stops timer, button B shows the measures times and resets.

16. xmas.py: A christmas tree animation.

## Built With

* [Mu Editor](https://codewith.mu/)

## Authors

* **Dimitris Nikolos** - [github](https://github.com/dimnikolos), [twitter](https://twitter.com/dnikolos)

## Acknowledgments

* Inspiration from [martinohanlon](https://github.com/martinohanlon/microbit-micropython)

* Deck of cards from (https://stackoverflow.com/questions/41970795/what-is-the-best-way-to-create-a-deck-of-cards)

* Quotes from (https://www.hollywoodreporter.com/lists/best-movie-quotes-hollywoods-top-867142/item/i-will-find-you-i-867115)
