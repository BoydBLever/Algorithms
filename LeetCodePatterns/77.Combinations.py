# https://leetcode.com/problems/combinations/
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def backtrack(start, path):
            # Early pruning: if the remaining elements plus current path size < k, no need to proceed
            if len(path) + (n - start + 1) < k:
                return
            if len(path) + (n - start + 1) < k:
                return
            # If the path contains 'k' elements, add it to the result
            if len(path) == k:
                res.append(path.copy())
                return

            # Explore further elements to add to the current combination
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()  # Backtrack

        backtrack(1, [])
        return res

# Decision tree for n = 4, k = 2
#                          []
#           /        |            \             \
#         [1]          [2]         [3]         [4]
#       / \ \        /  \           |      
#  [1,2][1,3][1,4] [2,3][2,4]     [3,4]      