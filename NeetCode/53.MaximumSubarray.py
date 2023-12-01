# https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algorithm: O(n) 
        maxSum = nums[0] # max subarray sum, initialized to the first element
        curSum = 0 # current subarray sum, initialized to 0

        for n in nums:
            curSum = max(curSum, 0) # reset curSum to zero if it is negative
            curSum += n # add the current element to curSum
            maxSum = max(maxSum, curSum) # update maxSum if curSum is greater
        return maxSum
    
# Whenever the current sum becomes greater than the maximum sub encountered so far, it updates the maxium sum. If the current sum becomes negative, it resets the current sum to 0.

nums = [-2, 1, -3]
maxSum = -2
curSum = 0

for n in nums:
    curSum = max(curSum, 0) -> curSum = 0
    curSum += n -> 1
    maxSum = max(maxSum, curSum) - > max(-2, 1)
return maxSum

# Cubed solution
for(i = 0 to n -1) -> first loop (i): each iteration chooses a new starting point for the subarray
for (j = i to n -1) -> second loop (j): 
for (k = i to j)
compute sum