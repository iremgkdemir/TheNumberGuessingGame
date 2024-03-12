# Number Guessing Game

Welcome to the Number Guessing Game! This simple Python game generates a random number between 1 and 100, and your task is to guess that number within a limited number of attempts.

## How to Play

1. Run the Python script (`number_guessing_game.py`).
2. Follow the instructions to choose the difficulty level - 'easy' or 'hard'.
   - If you choose 'easy', you will get 5 additional attempts.
   - If you choose 'hard', you will play with the default number of attempts.
3. The game will notify you of the remaining attempts and prompt you to make a guess.
4. Enter your guess, and the game will provide feedback if your guess is too low or too high.
5. Keep guessing until you either correctly guess the number or run out of attempts.

## Game Over

- If you correctly guess the number, the game will congratulate you and reveal the answer.
- If you run out of attempts, the game will inform you of the correct answer.

## Dependencies

This game uses the `random` module for generating random numbers, the `art` module for displaying the game logo, and the `replit` module for clearing the console screen.

## How to Run

Ensure you have the necessary dependencies installed:
```bash
pip install art replit
