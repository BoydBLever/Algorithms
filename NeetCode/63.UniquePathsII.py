class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        # # Brute Force : Dynamic Programming : DFS
        # M, N = len(grid), len(grid[0]) # dimensions of the grid
        # dp = {(M - 1, N - 1): 1} # hash map to use as our cache
        # # set the bottom right position to be 1
        
        # def dfs(r, c):
        #     if r == M or c == N or grid[r][c]:
        #         return 0
        #     if (r, c) in dp:
        #         return dp[(r , c)]
        #     dp[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
        #     return dp[(r, c)]

        # return dfs(0, 0)
        
        M, N = len(grid), len(grid[0])
        dp = [0] * N
        dp[N-1] = 1

        # Time: O(M * N), Space: O(N)
        for r in reversed(range(M)):
            for c in reversed(range(N)):
                if grid[r][c]:
                    dp[c] = 0
                elif c + 1 < N:
                    dp[c] = dp[c] + dp[c + 1]
        return dp[0]