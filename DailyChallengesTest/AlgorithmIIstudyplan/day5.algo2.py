# https://leetcode.com/problems/subarray-product-less-than-k/description/?envType=study-plan&id=algorithm-ii
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0
        
        count = 0
        product = 1
        left = 0
        
        for right in range(len(nums)):
            product *= nums[right]
            while product >= k:
                product /= nums[left]
                left += 1
            count += right - left + 1
        
        return count
# The time complexity of this solution is O(n), where n is the length of nums. We iterate through nums once and perform constant time operations at each step. The space complexity is also O(1), since we only need to store a constant number of variables.

# The idea behind the sliding window technique is to keep track of the product of the elements in the current window of nums. We start by initializing the product to 1 and the left pointer to 0. We then iterate through nums using the right pointer, updating the product at each step. If the product is greater than or equal to k, we move the left pointer to the right and divide the product by the element at the left pointer until the product is less than k. We then add the number of contiguous subarrays with right endpoint at the current position to the count, which is equal to right - left + 1. We continue this process until we have processed all the elements in nums.