class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Initial check
        if len(nums) < k:
            return 0
        # Initialize the sum
        sum = 0
        # Iterate k times to get the sum of the first k elements
        for i in range(k):
            sum += nums[i]
        # Initialize the max sum
        maxSum = sum
        # Iterate from k to the end of the array
        for i in range(k, len(nums)):
            # Add the current element to the sum
            sum += nums[i]
            # Subtract the first element from the sum
            sum -= nums[i - k]
            # Update the max sum
            maxSum = max(maxSum, sum)
        # Return the average
        return maxSum / k