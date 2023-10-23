# This code defines a recursive depth-first search (DFS) function to count the unique paths from the top left to the bottom right of a matrix, where movement is only allowed on cells containing a '0' and each cell can only be visited once.
# Count paths (backtracking)
from typing import grid

def dfs(grid, r, c, visit):
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

print(dfs(grid, 0, 0, set()))
