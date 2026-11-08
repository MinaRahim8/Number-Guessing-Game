# Number Guessing Game

A simple command-line number guessing game written in Python. The computer picks a random number between 1 and 100, and you try to guess it in as few attempts as possible. After each guess, the game tells you whether you were too high or too low.

## Features

- Random secret number (1–100) generated each round
- Personalized prompts using the player's name
- "Too high" / "too low" hints after every guess
- Handles non-numeric input on the first guess without crashing
- Option to play again with a new number

## Requirements

- Python 3.6 or newer (uses f-strings)
- No external libraries; only the built-in `random` module

## How to Run

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python number_guessing.py
   ```

   On some systems, use `python3` or `py` instead of `python`.

## How to Play

1. Enter your name when prompted.
2. Type a whole number and press Enter.
3. Use the hints to narrow down your next guess.
4. When you guess correctly, choose `yes` to play again or `no` to quit.

### Example

```
Welcome to the Number Guessing Game!
Try to guess a number between 1-100 in a the fewest guesses possible.
What is your name? Mina
Okay Mina, what is your guess? 50
Thats too high
Okay Mina, what is your next guess? 25
Thats too low
Okay Mina, what is your next guess? 37
Thats correct!
Play Again? Type yes/no :  no
Exiting game. Thank you for playing
```

## Project Structure

```
number_guessing.py   # Game source code
README.md            # Project documentation
```

### Functions

| Function | Description |
|---|---|
| `is_correct_number(val, secret)` | Returns `True` if the guess matches the secret number |
| `return_hint(val, secret)` | Returns a "too low" or "too high" hint string |
| `main()` | Runs the game loop: input, hints, and replay |

## Possible Improvements

- Track and display the number of attempts per round
- Keep a best score across rounds
- Add difficulty levels with different number ranges
- Validate input on every guess, not just the first

## Author

Mina
