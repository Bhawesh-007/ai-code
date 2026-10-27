# Capacities: Jug A = 4L, Jug B = 3L; Target: Jug A = 2L
CAP_A, CAP_B = 4, 3

def dfs_water_jug(state, visited, path):
    a, b = state
    path.append(state)
    visited.add(state)

    if a == 2:
        return True

    # Possible state transitions
    next_states = [
        (CAP_A, b),            # Fill A
        (a, CAP_B),            # Fill B
        (0, b),                # Empty A
        (a, 0),                # Empty B
        (a - min(a, CAP_B - b), b + min(a, CAP_B - b)), # Pour A -> B
        (a + min(b, CAP_A - a), b - min(b, CAP_A - a))  # Pour B -> A
    ]

    for nxt in next_states:
        if nxt not in visited:
            if dfs_water_jug(nxt, visited, path):
                return True

    path.pop()
    return False

path = []
dfs_water_jug((0, 0), set(), path)

print("DFS Path to measure 2 litres in Jug A:")
for step in path:
    print(step)