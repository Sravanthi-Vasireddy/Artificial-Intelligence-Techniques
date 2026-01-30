from collections import deque


# 0 = free path
# 1 = obstacle
# T = tool (target)
# S = start (robot position)
grid = [
    ['S', 0,  0,  1,  0],
    [1,   1,  0,  1,  0],
    [0,   0,  0,  0,  0],
    [0,   1,  1,  1,  0],
    [0,   0,  'T', 0,  0]
]

rows, cols = len(grid), len(grid[0])

# Directions: up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def find_position(symbol):
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == symbol:
                return (i, j)
    return None

start = find_position('S')
tool = find_position('T')


def bfs(start, tool):
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        (x, y), path = queue.popleft()

        # If tool found
        if (x, y) == tool:
            return path

        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if (0 <= nx < rows and 0 <= ny < cols and
                (nx, ny) not in visited and grid[nx][ny] != 1):
                queue.append(((nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))
    return None


path = bfs(start, tool)

if path:
    print(" Path found! Robot can fetch the tool as follows:")
    for step in path:
        print(step, end=" -> ")
    print("TOOL 🛠️")
else:
    print(" No path to the tool found.")
