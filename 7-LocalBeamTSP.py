import random

cities = ['A', 'B', 'C', 'D']
distance_matrix = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}

def calculate_distance(tour):
    dist = 0
    for i in range(len(tour)):
        dist += distance_matrix[tour[i]][tour[(i + 1) % len(tour)]]
    return dist

def get_neighbors(tour):
    neighbors = []
    for i in range(len(tour)):
        for j in range(i + 1, len(tour)):
            neighbor = tour.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

def local_beam_search(k=3, max_iterations=100):
    # Initial beam of k random tours starting from 'A'
    other_cities = cities[1:]
    beam = []
    for _ in range(k):
        t = ['A'] + random.sample(other_cities, len(other_cities))
        if t not in beam:
            beam.append(t)

    best_tour = min(beam, key=calculate_distance)
    best_dist = calculate_distance(best_tour)

    for _ in range(max_iterations):
        all_neighbors = []
        for tour in beam:
            all_neighbors.extend(get_neighbors(tour))

        # Select k best unique neighbors
        unique_neighbors = []
        for n in all_neighbors:
            if n not in unique_neighbors:
                unique_neighbors.append(n)

        sorted_neighbors = sorted(unique_neighbors, key=calculate_distance)
        beam = sorted_neighbors[:k]

        current_best = beam[0]
        current_dist = calculate_distance(current_best)

        if current_dist < best_dist:
            best_tour = current_best
            best_dist = current_dist

    return best_tour, best_dist

k = 3
best_tour, dist = local_beam_search(k)
print(f"Initial Beam Width (k): {k}")
print("Best Tour:")
print(" → ".join(best_tour) + " → " + best_tour[0])
print(f"Total Distance: {dist}")