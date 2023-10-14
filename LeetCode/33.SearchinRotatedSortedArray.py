# https://leetcode.com/problems/search-in-rotated-sorted-array/
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize two pointers: left at the beginning and right at the end of the array
        left, right = 0, len(nums) - 1
        
        # Continue the search while left pointer is less than or equal to the right pointer
        while left <= right:
            # Calculate the middle index
            mid = (left + right) // 2
            
            # If the target is found, return its index
            if nums[mid] == target:
                return mid
            
            # Check if the left half is sorted
            if nums[left] <= nums[mid]:
                # If target is within the left sorted half, adjust the right pointer
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                # If target is not in the left sorted half, adjust the left pointer
                else:
                    left = mid + 1
            # Check if the right half is sorted
            else:
                # If target is within the right sorted half, adjust the left pointer
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                # If target is not in the right sorted half, adjust the right pointer
                else:
                    right = mid - 1
        
        # If the target is not found in the list, return -1
        return -1

# Testing the function on a couple of examples
test_cases_13 = [
    ([4,5,6,7,0,1,2], 0, 4),
    ([4,5,6,7,0,1,2], 3, -1)
]

results_13 = [(test[:-1], Solution().search(*test[:-1]) == test[-1]) for test in test_cases_13]
results_13
#Neetcode solution
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (1 + r) // 2
            if target == nums[mid]:
                return mid
            
            #left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    left = mid + 1
                else:
                    r = mid - 1
            #right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return -1