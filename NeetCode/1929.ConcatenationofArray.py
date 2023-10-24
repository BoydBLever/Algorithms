# https://leetcode.com/problems/concatenation-of-array/
# NeetCode solution
from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # iterate through every value in the input array
        # take each of those values, and append it to the original array
        ans = []

        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans