# https://leetcode.com/problems/3sum/
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the input list
        nums.sort()
        
        # Initialize an empty list to store the results
        res = []
        
        # Iterate through the list
        for i in range(len(nums)):
            # Avoid duplicates by skipping the iteration if the current element is the same as the previous one
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Initialize two pointers, left and right
            left, right = i + 1, len(nums) - 1
            
            # Continue until the left pointer is less than the right pointer
            while left < right:
                # Calculate the current sum of three numbers
                s = nums[i] + nums[left] + nums[right]
                
                # If the sum is less than 0, move the left pointer to the right
                if s < 0:
                    left += 1
                # If the sum is greater than 0, move the right pointer to the left
                elif s > 0:
                    right -= 1
                # If the sum is 0, append the triplet to the results list
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    # Move both left and right pointers to avoid duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        
        return res

# Testing the function on given examples
test_cases_6 = [
    ([-1,0,1,2,-1,-4], [[-1,-1,2], [-1,0,1]]),
    ([0,1,1], []),
    ([0,0,0], [[0,0,0]])
]

results_6 = [(test[0], Solution().threeSum(test[0]) == test[1]) for test in test_cases_6]
results_6


#Neetcode solution
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         nums.sort()

#     for i, a in enumerate(nums):
#         if i > 0 and a == nums[i - 1]:
#             continue

#         l, r = i + 1, len(nums) - 1
#         while l < r:
#             threeSum = a + nums[l] + nums[r]
#             if threeSum > 0:
#                 r -= 1
#             elif threeSum < 0:
#                 l += 1
#             else:
#                 res.append([a, nums[l], nums[r]])
#                 l += 1
#                 while nums[l] == nums[l - 1]:
#                     l += 1
#         return res