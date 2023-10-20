# NeetCode solution
# https://leetcode.com/problems/target-sum/
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} # mapping a pair of values, (index, total) -> # of ways

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]
            
            dp[(i, total)] = (backtrack(i + 1, total + nums[i]) +
                             backtrack(i + 1, total - nums[i]))
            return dp[(i, total)]

        return backtrack(0, 0)