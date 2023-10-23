# Problem Statement (Matrix - BFS):
# Q: Find the length of the shortest path from the top left of the grid to the bottom right.

# Shortest path from top left to bottom right
from collections import deque

def bfs(grid):
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()
    queue = deque()
    queue.append((0, 0))
    visit.add((0, 0))

    length = 0

    while queue:
        for i in range(len(queue)):
            r, c = queue.popleft()
            if r == ROWS - 1 and c == COLS - 1:
                return length

            neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in neighbors:
                if (min(r + dr, c + dc) < 0 or 
                    r + dr == ROWS or c + dc == COLS or 
                    (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1):
                    continue

                queue.append((r + dr, c + dc))
                visit.add((r + dr, c + dc))

        length += 1

    return -1  # Path doesn't exist

grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 0]
]

print(bfs(grid))