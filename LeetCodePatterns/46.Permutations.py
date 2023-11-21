class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(path):
            # Base case: once a complete permutation is formed
            if len(path) == len(nums):
                res.append(path)
                return
            for num in nums:
                if num not in path:  # Check if the num is already in the current path
                    backtrack(path + [num])

        backtrack([])
        return res
    # Time: O(n!) n! permutations 
    # Space: O(n) recursion stack

# Decision Tree for nums = [1, 2, 3]
#                    []
#         /        |         \
#       [1]       [2]        [3]
#    /     \     /    \     /    \
#  [1,2]  [1,3] [2,1] [2,3] [3,1] [3,2]
#   |        |    |       |    |       |
# [1,2,3] [1,3,2] [2,1,3] [2,3,1] [3,1,2] [3,2,1]