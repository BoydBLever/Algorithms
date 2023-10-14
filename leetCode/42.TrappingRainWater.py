# https://leetcode.com/problems/trapping-rain-water/
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # If the height list is empty or contains less than 3 bars, return 0 as no water can be trapped
        if not height or len(height) < 3:
            return 0
        
        # Initialize two pointers: left and right at the beginning and end of the array, respectively
        left, right = 0, len(height) - 1
        
        # Initialize the left maximum and right maximum to the first and last bar's height, respectively
        left_max, right_max = height[left], height[right]
        
        # Initialize the trapped water to 0
        trapped_water = 0
        
        # Continue until the left pointer is less than or equal to the right pointer
        while left <= right:
            # Update left maximum and right maximum
            left_max, right_max = max(left_max, height[left]), max(right_max, height[right])
            
            # If the left maximum is less than the right maximum
            if left_max < right_max:
                # Add the difference between left maximum and current left height to trapped water
                trapped_water += left_max - height[left]
                # Move the left pointer to the right
                left += 1
            else:
                # Add the difference between right maximum and current right height to trapped water
                trapped_water += right_max - height[right]
                # Move the right pointer to the left
                right -= 1
        
        return trapped_water

# Testing the function on given examples
test_cases_8 = [
    ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
    ([4,2,0,3,2,5], 9)
]

results_8 = [(test[0], Solution().trap(test[0]) == test[1]) for test in test_cases_8]
results_8

#Neetcode solution
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         if not height: return 0

#         l, r = 0, len(height) - 1
#         leftMax, rightMax = height[1], height[r]
#         res = 0

#         while l < r:
#             if leftMax < rightMax
#                 1 += 1
#                 leftMax = max(leftMax, height[l])
#                 res += leftMax - height[l]
#             else:
#                 r -= 1
#                 rightMax = max(rightMax, height[r])
#                 res += rightMax - height[r]

#         return res