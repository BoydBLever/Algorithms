class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            # base case
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                return 0
    
            if grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            return 1 + dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1)
        
        max_area = 0
        # Visit every single position in the grid. Let's iterate through each row and column.
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # If we find a 1, then we have found an island. Let's DFS from that position.
                max_area = max(max_area, dfs(r, c))
        return max_area