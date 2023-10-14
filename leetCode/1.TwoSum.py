# https://leetcode.com/problems/two-sum/
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    # check for combinations that sum up to target
    # hashmap, mapping value to the index (val : index)
        prevMap = {} # val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return