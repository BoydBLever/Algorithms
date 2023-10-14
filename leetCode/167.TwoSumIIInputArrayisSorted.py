# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers, left at the beginning and right at the end of the array.
        left, right = 0, len(numbers) - 1
        
        # Continue until the left pointer is less than the right pointer.
        while left < right:
            # Calculate the current sum of numbers at left and right pointers.
            current_sum = numbers[left] + numbers[right]
            
            # If the current sum equals the target, return the indices incremented by one (since it's 1-indexed).
            if current_sum == target:
                return [left + 1, right + 1]
            # If the current sum is less than the target, move the left pointer to the right.
            elif current_sum < target:
                left += 1
            # If the current sum is greater than the target, move the right pointer to the left.
            else:
                right -= 1
        
        # If no solution is found, return an empty list (though the problem guarantees a solution).
        return []

# Testing the function on given examples
test_cases_5 = [
    ([2,7,11,15], 9, [1,2]),
    ([2,3,4], 6, [1,3]),
    ([-1,0], -1, [1,2])
]

results_5 = [(test[:-1], Solution().twoSum(*test[:-1]) == test[-1]) for test in test_cases_5]
results_5

#Neetcode solution
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         l, r = 0, len(numbers) - 1
    
#     while l < r:
#         curSum = numbers[1] + numbers[r]

#         if curSum > target:
#             r -= 1
#         elif curSum < target:
#             1 += 1
#         else:
#             return [1 + 1, r + 1]
#     return []
