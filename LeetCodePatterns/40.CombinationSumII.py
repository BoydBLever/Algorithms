# https://leetcode.com/problems/combination-sum-ii/description/
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, path, remaining):
            if remaining == 0:
                res.append(path.copy())
                return
            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                path.append(candidates[i])
                backtrack(i + 1, path, remaining - candidates[i])
                path.pop()

        candidates.sort()  # Sort the candidates to handle duplicates
        res = []
        backtrack(0, [], target)
        return res
# Decision Tree for sorted candidates = [1, 1, 2, 5, 6, 7, 10], target = 8
#                                []
#                   /     |     |     |     |     |     \
#                 [1]    [1*]  [2]   [5]   [6]   [7]   [10]
#                / | \    X    / ... / | \   |     |     X
#             [1,1] [1,2]    ...   [5,6] [5,7]  (end)  
#             /  ...    | \      ...
#          [1,1,2] ... [1,2,5]  ...
#          / ...      ...
#       [1,1,2,5] ...
# Root Node (Empty Set): Start with [].
# First Level of Decisions: Choose to start with each candidate.
# Handling Duplicates: [1*] represents the second 1, which is a duplicate. This path needs special handling to avoid duplicate combinations.
# Subsequent Levels: Keep adding candidates to the current path, considering the sum.
# Pruning: If the sum exceeds 8, stop exploring that branch.
# Valid Combinations: Paths like [1, 1, 6], [1, 7], [1, 1, 2, 5], [2, 6], etc., are valid as they sum up to 8.