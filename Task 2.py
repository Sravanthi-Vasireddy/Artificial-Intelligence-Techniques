import random
import math


def distance(p1, p2):
    """Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def total_distance(route, locations):
    """Compute total distance of the route starting and ending at depot (0)."""
    dist = 0
    current = 0  # start from depot
    for city in route:
        dist += distance(locations[current], locations[city])
        current = city
    dist += distance(locations[current], locations[0])  # return to depot
    return dist

def get_neighbor(route):
    """Generate a neighbor route by swapping two cities."""
    new_route = route[:]
    i, j = random.sample(range(len(route)), 2)
    new_route[i], new_route[j] = new_route[j], new_route[i]
    return new_route


def hill_climbing(locations, iterations=1000):
    n = len(locations) - 1  # excluding depot
    current_route = list(range(1, n + 1))
    random.shuffle(current_route)
    current_cost = total_distance(current_route, locations)

    best_route = current_route[:]
    best_cost = current_cost

    for _ in range(iterations):
        neighbor = get_neighbor(current_route)
        neighbor_cost = total_distance(neighbor, locations)

        # If the neighbor is better, move there
        if neighbor_cost < current_cost:
            current_route = neighbor
            current_cost = neighbor_cost

            # Track the best found so far
            if current_cost < best_cost:
                best_route = current_route[:]
                best_cost = current_cost

    return best_route, best_cost


# Depot + 5 delivery locations (x, y)
locations = [
    (50, 50),  # Depot
    (20, 40),
    (30, 10),
    (60, 20),
    (80, 80),
    (10, 70)
]

best_route, best_cost = hill_climbing(locations, iterations=5000)

print("Best Route Found:", [0] + best_route + [0])
print("Total Distance:", round(best_cost, 2))
