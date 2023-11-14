# Matrix (2D Grid)
grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]

# Count paths (backtracking)
def dfs(grid, r, c, visit):
    # Set up base cases, check if out of bounds, or if we've visited this cell, or if this cell is a wall, or if we've reached the end, and return 0 or 1 accordingly. 0 means no path, 1 means path.
    ROWS, COLS = len(grid), len(grid[0])
    # Check if out of bounds, or if we've visited this cell, or if this cell is a wall
    if (min(r, c) < 0 or
        r == ROWS or c == COLS or
        (r, c) in visit or grid[r][c] == 1):
        return 0
    # Check if we've reached the end
    if r == ROWS - 1 and c == COLS - 1:
        return 1
    # Mark this cell as visited
    visit.add((r, c))

    # Recursively call dfs on all 4 directions
    count = 0
    count += dfs(grid, r + 1, c, visit)
    count += dfs(grid, r - 1, c, visit)
    count += dfs(grid, r, c + 1, visit)
    count += dfs(grid, r, c - 1, visit)

    # Unmark this cell as visited
    visit.remove((r, c))
    return count

print(dfs(grid, 0, 0, set()))

# Visualize the grid
# 0 0 0 0
# 1 1 0 0
# 0 0 0 1
# 0 1 0 0