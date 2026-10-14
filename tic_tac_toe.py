"""Tic-Tac-Toe for two players in the terminal."""

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6),             # diagonals
]


class Board:
    def __init__(self):
        self.cells = [" "] * 9

    def show(self):
        rows = []
        for start in (0, 3, 6):
            rows.append(" " + " | ".join(self.cells[start:start + 3]))
        print("\n" + "\n---+---+---\n".join(rows) + "\n")

    def is_free(self, index):
        return self.cells[index] == " "

    def place(self, index, symbol):
        self.cells[index] = symbol

    def winner(self):
        for a, b, c in WIN_LINES:
            if self.cells[a] != " " and self.cells[a] == self.cells[b] == self.cells[c]:
                return self.cells[a]
        return None

    def is_full(self):
        return " " not in self.cells


def ask_move(board, symbol):
    while True:
        answer = input(f"Player {symbol}, choose a field (1-9): ").strip()
        if not answer.isdigit() or not 1 <= int(answer) <= 9:
            print("Please enter a number from 1 to 9.")
            continue
        index = int(answer) - 1
        if not board.is_free(index):
            print("That field is already taken.")
            continue
        return index


def play_round():
    board = Board()
    symbol = "X"
    print("Fields are numbered 1-9, left to right, top to bottom.")
    while True:
        board.show()
        board.place(ask_move(board, symbol), symbol)
        if board.winner():
            board.show()
            print(f"Player {symbol} wins!")
            return symbol
        if board.is_full():
            board.show()
            print("It's a draw.")
            return None
        symbol = "O" if symbol == "X" else "X"


def main():
    print("Welcome to Tic-Tac-Toe!")
    scores = {"X": 0, "O": 0}
    while True:
        winner = play_round()
        if winner:
            scores[winner] += 1
        print(f"Score - X: {scores['X']}  O: {scores['O']}")
        if input("Play again? (y/n): ").strip().lower() != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
