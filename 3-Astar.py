from queue import PriorityQueue

goal = ((1, 2, 3),
        (4, 5, 6),
        (7, 8, 0))

start = ((1, 2, 3),
         (4, 0, 6),
         (7, 5, 8))

# Heuristic: Number of misplaced tiles
def heuristic(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count

# Find blank tile
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate neighboring states
def neighbors(state):
    x, y = find_blank(state)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    result = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            temp = [list(row) for row in state]
            temp[x][y], temp[nx][ny] = temp[nx][ny], temp[x][y]
            result.append(tuple(tuple(row) for row in temp))
    return result

# A* Search
def a_star(start):
    pq = PriorityQueue()
    pq.put((heuristic(start), 0, start))
    visited = set()
    parent = {start: None}

    while not pq.empty():
        f, g, current = pq.get()
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        if current in visited:
            continue
        visited.add(current)

        for nxt in neighbors(current):
            if nxt not in visited:
                parent[nxt] = current
                new_g = g + 1
                new_f = new_g + heuristic(nxt)
                pq.put((new_f, new_g, nxt))
    return None

# Run A*
solution = a_star(start)
if solution:
    print("Solution found in", len(solution) - 1, "moves:\n")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found.")