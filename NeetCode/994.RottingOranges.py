from typing import List, collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        queue = collections.deque()
        fresh = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2:
                    queue.append((r, c))
                if val == 1:
                    fresh += 1
        if fresh == 0: return 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minutes = 0
        while queue:
            minutes += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
        return minutes - 1 if fresh == 0 else -1
