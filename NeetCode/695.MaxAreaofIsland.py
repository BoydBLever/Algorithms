from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (r < 0 or r == rows
                or c < 0 or c == cols
                or grid[r][c] == 0
                or (r, c) in visit):
                return 0
        
            visit.add((r, c))
            # Run DFS on all 4 directions
            return 1 + dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1)
        
        area = 0
        # Visit every single position in the grid. Let's iterate through each row and column.
        for r in range(rows):
            for c in range(cols):
                # If we find a 1, then we have found an island. Let's DFS from that position.
                area = max(area, dfs(r, c))
        return area
    
    # Time complexity: O(R*C) where R is the number of rows in the given grid, and C is the number of columns. We visit every square once.
    # Space complexity: O(R*C), the space used by the call stack during our recursion.
    # Test processing function 
    
    def test(self):
        input = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,1,1,0,1,0,0,0,0,0,0,0,0],
                [0,1,0,0,1,1,0,0,1,0,1,0,0],
                [0,1,0,0,1,1,0,0,1,1,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,0,0,0,0,0,0,1,1,0,0,0,0]]
        # Test case 1
        # Expected output: 6
        print(self.maxAreaOfIsland(input))

solution = Solution()
solution.test()