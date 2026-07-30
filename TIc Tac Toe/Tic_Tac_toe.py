import numpy as np

# Initialize board
board = np.array([['-', '-', '-'],
                  ['-', '-', '-'],
                  ['-', '-', '-']])

p1s = 'X'
p2s = 'O'


def print_board():
    print("\nCurrent Board:")
    for row in board:
        print(" | ".join(row))
    print()


def check_rows(symbol):
    for r in range(3):
        if all(board[r][c] == symbol for c in range(3)):
            print(symbol, "won 🎉")
            return True
    return False


def check_cols(symbol):
    for c in range(3):
        if all(board[r][c] == symbol for r in range(3)):
            print(symbol, "won 🎉")
            return True
    return False


def check_diagonals(symbol):
    if all(board[i][i] == symbol for i in range(3)) or \
       all(board[i][2-i] == symbol for i in range(3)):
        print(symbol, "won 🎉")
        return True
    return False


def won(symbol):
    return check_rows(symbol) or check_cols(symbol) or check_diagonals(symbol)


def place(symbol):
    while True:
        try:
            row = int(input(f"{symbol}'s turn → Enter row (1-3): ")) - 1
            col = int(input(f"{symbol}'s turn → Enter column (1-3): ")) - 1

            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == '-':
                board[row][col] = symbol
                break
            else:
                print("❌ Invalid move! Try again.")
        except ValueError:
            print("⚠️ Please enter numbers only (1-3).")


def play():
    print("Welcome to Tic Tac Toe! 🎮")
    print_board()

    for turn in range(9):
        if turn % 2 == 0:
            place(p1s)
        else:
            place(p2s)

        print_board()

        if turn % 2 == 0 and won(p1s):
            return
        elif turn % 2 == 1 and won(p2s):
            return

    print("It's a Draw! 🤝")


# Run the game
play()
