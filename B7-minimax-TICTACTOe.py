import math

def check_winner(board):
    win_states = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for state in win_states:
        a, b, c = state
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    if " " not in board:
        return "Draw"
    return None

def minimax(board, depth, is_max):
    result = check_winner(board)
    if result == "O":
        return 1
    elif result == "X":
        return -1
    elif result == "Draw":
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best = min(best, score)
        return best

def best_move(board):
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

def print_board(board):
    print()
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
    print()

board = [" "] * 9

while True:
    print_board(board)
    pos = int(input("Enter your move (0-8): "))
    if pos < 0 or pos > 8 or board[pos] != " ":
        print("Invalid move!")
        continue
    board[pos] = "X"
    if check_winner(board):
        break
    ai = best_move(board)
    board[ai] = "O"
    if check_winner(board):
        break

print_board(board)
result = check_winner(board)
if result == "Draw":
    print("Game Draw!")
else:
    print(result, "wins!")