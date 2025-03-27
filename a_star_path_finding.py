import heapq

# Define the grid
grid = [
    ['S', '.', '.', '#'],
    ['.', '#', '.', '.'],
    ['.', '.', '.', 'G'],
]

# Directions: up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def find_point(symbol):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == symbol:
                return (y, x)
    return None

def a_star(start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        for dy, dx in directions:
            neighbor = (current[0] + dy, current[1] + dx)
            y, x = neighbor

            if 0 <= y < len(grid) and 0 <= x < len(grid[0]) and grid[y][x] != '#':
                tentative_g = g_score[current] + 1
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score, neighbor))
                    came_from[neighbor] = current

    return None  # No path found

def print_grid(path):
    visual = [row[:] for row in grid]  # deep copy
    for y, x in path:
        if visual[y][x] not in ('S', 'G'):
            visual[y][x] = '*'
    for row in visual:
        print(' '.join(row))

# Run A*
start = find_point('S')
goal = find_point('G')
path = a_star(start, goal)

if path:
    print("\n✅ Path found!\n")
    print_grid(path)
else:
    print("\n❌ No path found.")

