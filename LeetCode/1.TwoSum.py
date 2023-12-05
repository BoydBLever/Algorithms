# https://leetcode.com/problems/two-sum/
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    # check for combinations that sum up to target
    # hashmap, map the number to its index
        prevMap = {} # val : index #Dictionaries in Python are implementations of hashmaps / hash tables. Store the number from the nums list as the key, and its index as the value.

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
    
# Other possible approach: brute force, hash map, two pointers.