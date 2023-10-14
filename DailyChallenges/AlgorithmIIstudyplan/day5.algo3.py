# https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=study-plan&id=algorithm-ii
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left = 0
        right = 0
        min_len = float('inf')
        curr_sum = 0
        
        while right < n:
            curr_sum += nums[right]
            while curr_sum >= target:
                min_len = min(min_len, right - left + 1)
                curr_sum -= nums[left]
                left += 1
            right += 1
        
        return min_len if min_len != float('inf') else 0
# One approach to solve this problem is to use a sliding window technique. We can start by initializing two pointers, left and right, both pointing to the first element of the array. We can then move the right pointer to the right until the sum of the subarray from left to right is greater than or equal to the target. Once we find such a subarray, we can update the length of the subarray as the minimum length found so far, and move the left pointer to the right until the sum of the subarray from left to right is less than the target again. We can then repeat this process until we reach the end of the array.
# In this implementation, we initialize the variables left, right, min_len, and curr_sum. We use left and right as the pointers to define the current subarray. min_len is the minimum length found so far, initialized as infinity. curr_sum is the current sum of the elements in the subarray from left to right.

# We then loop through the array using right as the index. In each iteration, we add the current element to curr_sum. If curr_sum is greater than or equal to the target, we enter the while loop and update the min_len as the minimum of the current min_len and the length of the current subarray. We then move the left pointer to the right until the sum of the subarray from left to right is less than the target again.

# We repeat this process until we reach the end of the array. Finally, we return the min_len if it is not infinity, or 0 otherwise.

# The time complexity of this solution is O(n), where n is the length of the array, since we are traversing the array once. The space complexity is O(1), since we are only using a constant amount of extra space.