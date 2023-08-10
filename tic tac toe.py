import math

# Define constants for the players
PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = " "

def print_board(board):
    print("-------------")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("-------------")

def evaluate(board):
    # Check rows, columns, and diagonals to see if any player has won
    for row in board:
        if row.count(PLAYER_X) == 3:
            return 10
        if row.count(PLAYER_O) == 3:
            return -10

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == PLAYER_X:
            return 10
        if board[0][col] == board[1][col] == board[2][col] == PLAYER_O:
            return -10

    if board[0][0] == board[1][1] == board[2][2] == PLAYER_X:
        return 10
    if board[0][0] == board[1][1] == board[2][2] == PLAYER_O:
        return -10

    if board[0][2] == board[1][1] == board[2][0] == PLAYER_X:
        return 10
    if board[0][2] == board[1][1] == board[2][0] == PLAYER_O:
        return -10

    # If no one has won, return 0 (tie)
    return 0

def is_moves_left(board):
    for row in board:
        if EMPTY in row:
            return True
    return False

def minimax(board, depth, is_maximizing, alpha, beta):
    score = evaluate(board)

    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if not is_moves_left(board):
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    best = max(best, minimax(board, depth + 1, False, alpha, beta))
                    board[i][j] = EMPTY
                    alpha = max(alpha, best)
                    if alpha >= beta:
                        break
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    best = min(best, minimax(board, depth + 1, True, alpha, beta))
                    board[i][j] = EMPTY
                    beta = min(beta, best)
                    if alpha >= beta:
                        break
        return best

def find_best_move(board):
    best_val = -math.inf
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                move_val = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = EMPTY
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)

    return best_move

def main():
    board = [[EMPTY, EMPTY, EMPTY] for _ in range(3)]

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while is_moves_left(board):
        x, y = None, None
        while x is None or y is None or board[x][y] != EMPTY:
            try:
                x, y = map(int, input("Enter row and column (0-2) separated by space: ").split())
            except ValueError:
                print("Invalid input. Try again.")

        board[x][y] = PLAYER_O
        print_board(board)

        if not is_moves_left(board):
            break

        best_move = find_best_move(board)
        board[best_move[0]][best_move[1]] = PLAYER_X
        print("AI's move:")
        print_board(board)

    score = evaluate(board)
    if score == 0:
        print("It's a tie!")
    elif score == 10:
        print("AI wins!")
    else:
        print("You win!")

if __name__ == "__main__":
    main()
