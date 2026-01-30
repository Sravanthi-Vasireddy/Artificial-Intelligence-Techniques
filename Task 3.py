import heapq
import math


def heuristic(a, b):
    """Euclidean distance heuristic."""
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


def a_star_search(graph, locations, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic(locations[start], locations[goal])
    
    while open_set:
        current = heapq.heappop(open_set)[1]
        
        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, g_score[goal]
        
        for neighbor, cost in graph[current]:
            tentative_g = g_score[current] + cost
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(locations[neighbor], locations[goal])
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return None, float('inf')


locations = {
    'A': (0, 0),
    'B': (2, 2),
    'C': (2, -2),
    'D': (5, 0),
    'E': (7, 3),
    'F': (7, -3)
}

# Graph connections: node -> [(neighbor, distance)]
graph = {
    'A': [('B', 3), ('C', 3)],
    'B': [('A', 3), ('D', 4), ('E', 6)],
    'C': [('A', 3), ('D', 4), ('F', 6)],
    'D': [('B', 4), ('C', 4), ('E', 3), ('F', 3)],
    'E': [('B', 6), ('D', 3), ('F', 5)],
    'F': [('C', 6), ('D', 3), ('E', 5)]
}


start = 'A'
goal = 'E'
path, distance = a_star_search(graph, locations, start, goal)

print("Optimal Path:", " → ".join(path))
print("Total Distance:", round(distance, 2))
