# https://leetcode.com/problems/remove-element/
# NeetCode solution
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #Initialization of Partitioning Pointer
        # The variable k is a pointer used to keep track of the position in the list nums where the next number (that is not equal to val) should be placed.
        k = 0

        # Iterating through the list
        for i in range(len(nums)):
            #if the current element is not equal to val, it means we want to keep this element in the final list
            if nums[i] != val:
                # Partitioning the list
                nums[k] = nums[i]
                k += 1
        return k