import math
import random



def distance(a, b):
    """Euclidean distance between two cities."""
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)



class AntColony:
    def __init__(self, locations, n_ants=10, n_iterations=100, decay=0.5, alpha=1, beta=3):
        self.locations = locations
        self.n_ants = n_ants
        self.n_iterations = n_iterations
        self.decay = decay  # pheromone evaporation
        self.alpha = alpha  # pheromone importance
        self.beta = beta    # distance importance
        self.n_cities = len(locations)
        self.dist_matrix = [[distance(locations[i], locations[j]) for j in range(self.n_cities)] for i in range(self.n_cities)]
        self.pheromone = [[1 for _ in range(self.n_cities)] for _ in range(self.n_cities)]

    def route_length(self, route):
        """Calculate total distance of a route."""
        total = 0
        for i in range(len(route) - 1):
            total += self.dist_matrix[route[i]][route[i + 1]]
        total += self.dist_matrix[route[-1]][route[0]]  # return to depot
        return total

    def choose_next_city(self, current_city, visited):
        """Choose next city using probability based on pheromone and distance."""
        probs = []
        pheromone_row = self.pheromone[current_city]
        for j in range(self.n_cities):
            if j not in visited:
                pheromone_strength = pheromone_row[j] ** self.alpha
                visibility = (1 / self.dist_matrix[current_city][j]) ** self.beta
                probs.append(pheromone_strength * visibility)
            else:
                probs.append(0)
        total = sum(probs)
        if total == 0:
            return random.choice([j for j in range(self.n_cities) if j not in visited])
        probs = [p / total for p in probs]
        return random.choices(range(self.n_cities), weights=probs, k=1)[0]

    def run(self):
        best_route = None
        best_length = float("inf")

        for iteration in range(self.n_iterations):
            all_routes = []
            all_lengths = []

            for _ in range(self.n_ants):
                route = [random.randint(0, self.n_cities - 1)]
                while len(route) < self.n_cities:
                    next_city = self.choose_next_city(route[-1], route)
                    route.append(next_city)
                length = self.route_length(route)
                all_routes.append(route)
                all_lengths.append(length)

                if length < best_length:
                    best_length = length
                    best_route = route

            # Pheromone evaporation
            for i in range(self.n_cities):
                for j in range(self.n_cities):
                    self.pheromone[i][j] *= (1 - self.decay)

            # Pheromone update based on best routes
            for route, length in zip(all_routes, all_lengths):
                contribution = 1 / length
                for i in range(len(route) - 1):
                    a, b = route[i], route[i + 1]
                    self.pheromone[a][b] += contribution
                    self.pheromone[b][a] += contribution
                # Return to depot
                self.pheromone[route[-1]][route[0]] += contribution
                self.pheromone[route[0]][route[-1]] += contribution

            print(f"Iteration {iteration+1}/{self.n_iterations} | Best Distance: {best_length:.2f}")

        return best_route, best_length



if __name__ == "__main__":
    # Define delivery locations (x, y)
    locations = [
        (0, 0),   # Depot
        (10, 3),
        (5, 8),
        (8, 12),
        (13, 7),
        (6, 2)
    ]

    colony = AntColony(locations, n_ants=20, n_iterations=50, decay=0.3, alpha=1, beta=4)
    best_route, best_distance = colony.run()

    print("\n🏁 Optimal Delivery Route Found:")
    print(" → ".join(str(city) for city in best_route), "→", best_route[0])
    print("📏 Total Distance:", round(best_distance, 2))
