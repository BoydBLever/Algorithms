# https://leetcode.com/problems/binary-search/
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize two pointers: left at the beginning and right at the end of the array.
        left, right = 0, len(nums) - 1
        
        # Continue the search while left pointer is less than or equal to the right pointer
        while left <= right:
            # Calculate the middle index
            mid = (left + right) // 2
            
            # If the target is found, return its index
            if nums[mid] == target:
                return mid
            # If the target is greater than the element at the middle index, move the left pointer to mid + 1
            elif nums[mid] < target:
                left = mid + 1
            # If the target is less than the element at the middle index, move the right pointer to mid - 1
            else:
                right = mid - 1
        
        # If the target is not found in the list, return -1
        return -1

# Testing the function on given examples
results_9 = [(test[:-1], Solution().search(*test[:-1]) == test[-1]) for test in test_cases_9]
results_9
#Neetcode solution
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         l, r = 0, len(nums) - 1

#         while l <= r:
#             m = (1 + r) // 2
#             if nums[m] > target:
#                 r = m - 1
#             elif nums[m] < target:
#                 l = m + 1
#             else:
#                 return m
#         return -1