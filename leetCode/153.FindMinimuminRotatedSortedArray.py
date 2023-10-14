# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # If the list contains only one element, return that element
        if len(nums) == 1:
            return nums[0]
        
        # Initialize two pointers: left at the beginning and right at the end of the array
        left, right = 0, len(nums) - 1
        
        # If the last element is greater than the first element, then there is no rotation
        if nums[right] > nums[0]:
            return nums[0]
        
        # Binary search to find the rotation point (minimum element)
        while left <= right:
            # Calculate the middle index
            mid = (left + right) // 2
            
            # If the mid element is greater than the next element, then mid+1 is the smallest
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            # If the mid element is smaller than the previous element, then mid is the smallest
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            
            # If the mid elements value is greater than the 0th element, move to the right side of mid
            if nums[mid] > nums[0]:
                left = mid + 1
            # If the mid elements value is less than or equal to the 0th element, move to the left side of mid
            else:
                right = mid - 1

# Testing the function on given examples
results_12 = [(test[0], Solution().findMin(test[0]) == test[1]) for test in test_cases_12]
results_12
#Neetcode solution
# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         res = nums[0]
#         l, r = 0, len(nums) - 1

#         while l <= r:
#             if nums[l] < nums[r]:
#                 res = min(res, nums[l])
#                 break

#             m = (l + r) // 2
#             res = min(res, nums[m])
#             if nums[m] >= nums[l]:
#                 l = m + 1
#             else:
#                 r = m - 1
#         return res