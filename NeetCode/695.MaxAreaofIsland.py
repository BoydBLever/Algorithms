class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == 0 or (r, c) in visit):
                return 0
        
            visit.add((r, c))
            return 1 + dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1)
        
        area = 0
        # Visit every single position in the grid. Let's iterate through each row and column.
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # If we find a 1, then we have found an island. Let's DFS from that position.
                area = max(area, dfs(r, c))
        return area