
from collections import defaultdict

class RobotTraversal:
    def __init__(self, graph):
        self.graph = graph  # adjacency list
        self.colors = {node: 0 for node in graph}  # 0 = unvisited, 1 = visited, 2 = obstacle
        self.traversal_path = []

    def add_obstacle(self, node):
        """Mark a node as obstacle."""
        if node in self.colors:
            self.colors[node] = 2

    def dfs_traverse(self, node):
        """Depth-First Traversal with coloring logic."""
        if self.colors[node] == 2:
            return  # skip obstacles
        if self.colors[node] == 1:
            return  # already visited

        # Color current node as visited (green)
        self.colors[node] = 1
        self.traversal_path.append(node)
        print(f" Visiting node {node} | Marked as GREEN")

        for neighbor in self.graph[node]:
            if self.colors[neighbor] == 0:
                self.dfs_traverse(neighbor)

    def display_colors(self):
        """Display final color states."""
        print("\n Final Node Colors:")
        for node, color in self.colors.items():
            status = " Visited" if color == 1 else (" Obstacle" if color == 2 else " Unvisited")
            print(f"Node {node}: {status}")

    def display_path(self):
        print("\n Robot Traversal Path:")
        print(" -> ".join(map(str, self.traversal_path)))



if __name__ == "__main__":
    # Graph adjacency list representation
    # Each node represents a position the robot can move to
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    robot = RobotTraversal(graph)

    # Add obstacles (restricted nodes)
    robot.add_obstacle('E')

    print(" Starting robot traversal from node A...\n")
    robot.dfs_traverse('A')

    # Show results
    robot.display_path()
    robot.display_colors()
