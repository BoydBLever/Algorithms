# https://leetcode.com/problems/concatenation-of-array/
# NeetCode solution
from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # iterate through every value in the input array
        # take each of those values, and append it to the original array
        ans = []

        # outer loop iterates twice for i = 0 and i = 1
        for i in range(2):
            # inner loop will iterate through each element in the nums list
            for n in nums:
                ans.append(n)
        return ans