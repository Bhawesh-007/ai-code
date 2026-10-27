# Model-Based Intelligent Agent for Grid Navigation
grid = [
    ['S', '.', '.', '#'],
    ['.', '#', '.', '.'],
    ['.', '.', '.', '#'],
    ['#', '.', '.', 'G']
]

rows = len(grid)
cols = len(grid[0])
start = (0, 0)
goal = (3, 3)

# Possible moves: Up, Down, Left, Right
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = set()

def is_valid(x, y):
    return (0 <= x < rows and
            0 <= y < cols and
            grid[x][y] != '#' and
            (x, y) not in visited)

current = start
visited.add(current)

print("Agent Path:")
print(current)

while current != goal:
    moved = False
    for dx, dy in moves:
        nx, ny = current[0] + dx, current[1] + dy
        if is_valid(nx, ny):
            current = (nx, ny)
            visited.add(current)
            print(current)
            moved = True
            break
    if not moved:
        print("No valid path found!")
        break

if current == goal:
    print("Goal Reached!")