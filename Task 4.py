import math



def print_board(board):
    print()
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("---------")
    print()

def is_moves_left(board):
    for row in board:
        if " " in row:
            return True
    return False

def evaluate(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return 10 if row[0] == "X" else -10

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return 10 if board[0][col] == "X" else -10

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return 10 if board[0][0] == "X" else -10

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return 10 if board[0][2] == "X" else -10

    return 0



def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    # Base cases
    if score == 10:
        return score - depth  # prefer quicker wins
    if score == -10:
        return score + depth  # prefer slower losses
    if not is_moves_left(board):
        return 0  # draw

    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = " "
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = " "
        return best



def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                move_val = minimax(board, 0, False)
                board[i][j] = " "

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Tic-Tac-Toe (You = O, AI = X)")
    print_board(board)

    while True:
        # Human move
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))

        if board[row][col] != " ":
            print("Invalid move! Try again.")
            continue

        board[row][col] = "O"
        print_board(board)

        if evaluate(board) == -10:
            print("🎉 You win!")
            break
        if not is_moves_left(board):
            print("It's a draw!")
            break

        # AI move
        print("AI is thinking...")
        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = "X"
        print_board(board)

        if evaluate(board) == 10:
            print("🤖 AI wins!")
            break
        if not is_moves_left(board):
            print("It's a draw!")
            break


if __name__ == "__main__":
    play_game()
