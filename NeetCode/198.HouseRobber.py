class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1 or len(nums) == 2:
            return max(nums)

        # dynamic programming approach
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[-1]
# Time Complexity: O(n)
# Space Complexity: O(n)
# Decision Tree for nums = [1, 2, 3]
#                    [Start]
#                  /        \
#               [1]          [0]       (Decision at House 1: Rob [1] or Skip [0])
#                |            |
#             [1,0]          [0,2]     (Decision at House 2: Must skip if robbed House 1)
#             /   \            |
#         [1,0,3] [1,0,0]    [0,2,0]   (Decision at House 3)