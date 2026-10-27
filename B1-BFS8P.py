from collections import deque

start_state = (
    (1, 2, 3),
    (4, 0, 6),
    (7, 5, 8)
)

goal_state = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)

def find_blank(state):
    for r in range(3):
        for c in range(3):
            if state[r][c] == 0:
                return r, c

def get_neighbors(state):
    r, c = find_blank(state)
    moves = [(-1, 0, "Up"), (1, 0, "Down"), (0, -1, "Left"), (0, 1, "Right")]
    neighbors = []
    for dr, dc, move in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            grid = [list(row) for row in state]
            grid[r][c], grid[nr][nc] = grid[nr][nc], grid[r][c]
            neighbors.append((tuple(tuple(row) for row in grid), move))
    return neighbors

def bfs(start, goal):
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        current, path = queue.popleft()
        if current == goal:
            return path, current

        for neighbor, move in get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [move]))
    return None, None

path, final = bfs(start_state, goal_state)
print("Shortest Path Found by BFS:")
print(" → ".join(path))
print("Total Moves =", len(path))