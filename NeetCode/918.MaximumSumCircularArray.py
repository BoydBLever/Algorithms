class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(gen):
            # Standard Kadane's algorithm
            curSum, maxSum = float('-inf'), float('-inf')
            for x in gen:
                curSum = x + max(curSum, 0)
                maxSum = max(maxSum, curSum)
            return maxSum

        # Case 1: get the maximum sum using standard Kadane's algorithm
        max_kadane = kadane(nums)
        
        # Case 2: find the maximum for wrap-around
        # Calculate the total sum and the minimum subarray sum
        total_sum = sum(nums)
        min_wrap = kadane(-num for num in nums)

        # Maximum subarray sum for wrap-around cases
        max_wrap = total_sum + min_wrap
        
        # Special case for all negative numbers
        if max_wrap == 0:
            return max_kadane

        # Return the maximum of the two cases
        return max(max_kadane, max_wrap)