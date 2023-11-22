# https://leetcode.com/problems/combination-sum-iii/
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start, path, remaining):
            # Check if the current combination is valid
            if len(path) == k and remaining == 0:
                res.append(path.copy())
                return
            
            # Early pruning
            if len(path) > k or remaining < 0:
                return

            # Explore further elements
            for i in range(start, 10):  # Numbers are from 1 to 9
                path.append(i)
                backtrack(i + 1, path, remaining - i)
                path.pop()  # Backtrack

        res = []
        backtrack(1, [], n)
        return res
# Decision Tree for k = 2, n = 4
#                            []
#           /    |    |    |    |    |    |    |    \
#         [1]   [2]   [3]  [4]  [5]  [6]  [7]  [8]  [9]
#        / | \  / | \  / \  X    X    X    X    X    X
#      [1,2][1,3][2,3]
#       /    |    \
#   (end)  (end)  [2,4]
#                 (end)
