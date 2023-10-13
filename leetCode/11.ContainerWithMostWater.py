# https://chat.openai.com/c/b1c7fbc0-e1d3-492e-aa19-e2a6b2c4ec94
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize two pointers: left at the beginning and right at the end of the array
        left, right = 0, len(height) - 1
        
        # Initialize max_area as 0
        max_area = 0
        
        # Continue until the left pointer is less than the right pointer
        while left < right:
            # Calculate the minimum height between the two pointers
            min_height = min(height[left], height[right])
            
            # Calculate the current area and update the max_area if needed
            max_area = max(max_area, min_height * (right - left))
            
            # Move the pointer that points to the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

# Testing the function on given examples
test_cases_7 = [
    ([1,8,6,2,5,4,8,3,7], 49),
    ([1,1], 1)
]

results_7 = [(test[0], Solution().maxArea(test[0]) == test[1]) for test in test_cases_7]
results_7
#Neetcode solution
class Solution:
    def maxArea(self, height: List[int]) -> int:
        #BRUTE FORCE (does not work)
        # res = 0

        # for l in range(len(height)):
        #     for r in range(l + 1, len(height)):
        #         area = (r - l) * min(height[l], height[r])
        #         res = max(res, area)

        #     return res
        #TWO POINTER TECHNIQUE: Linear time solution O(n)
        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return res
