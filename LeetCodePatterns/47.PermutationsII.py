# https://leetcode.com/problems/permutations-ii/description/
# Decision Tree for nums = [1, 1, 2]
#                  []
#         /      |      \
#       [1]     [1*]    [2]
#     /    \   (skip)   /   \
#  [1,1]  [1,2]       [2,1] [2,1*]
#    |       |         |     (skip)
# [1,1,2] [1,2,1]   [2,1,1]

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(path, nums):
            # Base case: once a complete permutation is formed
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue

                if not used[i]:
                    used[i] = True # Mark as used
                    backtrack(path + [nums[i]], nums)
                    used[i] = False # Backtrack: unmark
                
        used = [False] * len(nums)
        backtrack([], nums)
        return res
# Time complexity: O(n * n!)
# Space complexity: O(n * n!)