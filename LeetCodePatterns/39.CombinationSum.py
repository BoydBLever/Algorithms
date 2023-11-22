# https://leetcode.com/problems/combination-sum/
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, path, current_sum):
            # Check if the current sum equals the target
            if current_sum == target:
                res.append(path.copy())
                return
            # Stop if the sum exceeds the target
            if current_sum > target:
                return

            # Explore further elements
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, current_sum + candidates[i])
                path.pop()  # Backtrack

        res = []
        backtrack(0, [], 0)
        return res
# Decision Tree for candidates = [2, 3, 6, 7], target = 7
#                            []
#         /         |         |             \
#       [2]        [3]       [6]            [7]
#      / | \       / ...    (end)*pruning   (end)
#   [2,2][2,3]  ...
#    / 
# [2,2,2] ...