def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def get_candidates(board, row, col):
    if board[row][col] != 0:
        return []
    return [num for num in range(1, 10) if is_valid(board, row, col, num)]

# Constraint propagation: fill cells that have only 1 possible candidate
def propagate_constraints(board):
    changed = True
    while changed:
        changed = False
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:
                    candidates = get_candidates(board, r, c)
                    if len(candidates) == 1:
                        board[r][c] = candidates[0]
                        changed = True

def solve_sudoku(board):
    propagate_constraints(board)
    empty = None
    min_candidates = 10

    # Select cell with minimum remaining values (MRV heuristic)
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                candidates = get_candidates(board, r, c)
                if len(candidates) < min_candidates:
                    min_candidates = len(candidates)
                    empty = (r, c)

    if not empty:
        return True  # Solved

    row, col = empty
    candidates = get_candidates(board, row, col)

    for num in candidates:
        board[row][col] = num
        # Deep copy board to maintain state during recursion
        board_copy = [r[:] for r in board]
        if solve_sudoku(board_copy):
            for i in range(9):
                board[i] = board_copy[i]
            return True
        board[row][col] = 0

    return False

board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(board):
    print("Solved Sudoku:")
    for row in board:
        print(" ".join(str(num) for num in row))
else:
    print("No solution exists")