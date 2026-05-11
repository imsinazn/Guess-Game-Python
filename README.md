# 🎯 Guess Game – CLI Number Guessing Game

A terminal-based number guessing game with difficulty levels, dynamic scoring, and smart feedback.

## 🚀 Features

- **Three difficulty levels**: Easy (1-50), Medium (1-100), Hard (1-200)
- **Dynamic scoring**: Each guess costs 10 points, score never goes negative
- **Smart hints**: Detects when you're very close (difference ≤ 5)
- **Input validation**: Handles out-of-range and invalid inputs gracefully
- **No external dependencies**: Pure Python 3

## 🕹️ How to Play

1. Choose difficulty: `e`, `m`, or `h`
2. Set your number of allowed guesses
3. Guess the secret number
4. Each wrong guess costs 10 points
5. Get closer and win!

## Example
GUESS GAME
Choose the type of game
e = Easy , m = Medium , h = Hard     Choose: m
Your challenge was accepted !
Hint : Each guess is 10 point! If you make mistake you lose your point!
Enter your count of Guess = 5
YOU HAVE 5 CHANCE
READY???
Guess the number = 70
guess is lower than secret number! 4 is remaining
Guess the number = 90
guess is over but very near! 3 is remaining
Guess the number = 85
Well done! the number was 85 !
Your point is = 20

## 📦 Installation

```bash
git clone https://github.com/imsinazn/Guess-Game-Python.git
cd Guess-Game-Python
python game.py
