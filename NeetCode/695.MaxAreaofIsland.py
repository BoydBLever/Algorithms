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
            # Run DFS on all 4 directions. 
            # 1. Exploring adjacent cells: The recursive calls are made only if the position is land, and are made to explore the cells that are directly adjacent to the current cell - specifically, the cells above, below, to the left and to the right. This is consistent with the definition of an island in the problem, where cells are considered connected if they are horizontally or vertically adjacent (and not diagonally adjacent).
            # 2. Checking Land or Water: For each of these adjacent cells, the dfs function checks whether the cell is part of land and hasn't been visited yet. If the cell water, of has already been visited, then the function returns 0 (shown above in the if statement).
            # 3. Accumulating Area: When an adjacent cell is part of the island (land and not visited), the recursive call to dfs will further explore from that cell, and the return value will contribute to the total area of the island. The sum of these recursive calls, along with the 1 for the current cell, gives the total area of the island connected to the current cell.
            # 4. Marking Visited Cells: The current cell is marked as visited by adding it to the visited set. This ensures that the same cell isn't visited again.
            return 1 + dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1)
        
        area = 0
        # Iterate over every cell in the grid to check if it is land or water, and use the max function to keep track of the maximum area. Iterating over every cell in the grid ensures that we check every potential starting point of an island.
        # Main Function Loop
        for r in range(rows):
            for c in range(cols):
                # If we find a 1, then we have found an island. Let's DFS from that position. The dfs function returns the area of the island to which the cell belongs. The max function is used to update the area variable. It compares the current value of area with the area returned by the dfs call for the current cell. If the new area is larger than the current area, the new area is used as the value of area.
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