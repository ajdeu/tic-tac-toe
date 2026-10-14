# Building Tic-Tac-Toe in the Terminal with Python

I built a two-player Tic-Tac-Toe game that runs entirely in the terminal. It was a good exercise in combining classes, functions, loops and user input into one small program.

## The idea

Tic-Tac-Toe has simple rules, which let me focus on structure instead of game design. Two players, X and O, take turns choosing a field from 1 to 9 until someone gets three in a row or the board is full.

## How it works

- **`Board` class:** stores the nine fields in a list and knows how to print itself, place a symbol, check for a winner and detect a full board.
- **`WIN_LINES`:** the eight winning combinations (rows, columns, diagonals) are stored as index tuples, so checking for a winner is one short loop.
- **`ask_move()`:** uses `input()` in a loop and rejects anything that is not a number from 1 to 9 or that points at an occupied field.
- **`play_round()` and `main()`:** run a single round, keep a running score across rounds and ask whether to play again.

## What I learned

- Putting game state into a class keeps the rest of the code small and readable.
- Validating input in its own function made the main game loop much simpler.
- Committing in small steps with Git made it easy to see how the program grew.

## Run it yourself

```bash
python3 tic_tac_toe.py
```

Next steps could be a computer opponent or a bigger board.
