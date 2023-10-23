# This code defines a recursive depth-first search (DFS) function to count the unique paths from the top left to the bottom right of a matrix, where movement is only allowed on cells containing a '0' and each cell can only be visited once.
# Count paths (backtracking)
from typing import List, Set, Tuple

def dfs(grid: List[List[int]], r: int, c: int, visit: Set[Tuple[int, int]]) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    
    if (min(r, c) < 0 or
        r == ROWS or c == COLS or
        (r, c) in visit or grid[r][c] == 1):
        return 0

    if r == ROWS - 1 and c == COLS - 1:
        return 1

    visit.add((r, c))
    
    count = 0
    count += dfs(grid, r + 1, c, visit)
    count += dfs(grid, r - 1, c, visit)
    count += dfs(grid, r, c + 1, visit)
    count += dfs(grid, r, c - 1, visit)
    
    visit.remove((r, c))
    
    return count

# This is the grid.
grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 0]
]

print(dfs(grid, 0, 0, set()))

# This is a 4x4 matrix where cells containing a 1 represent blocked paths and cells with a 0 are open paths.