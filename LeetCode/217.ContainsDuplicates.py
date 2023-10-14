# https://leetcode.com/problems/contains-duplicate/
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # iterate through the array, and check for duplicates
        # 1. Initialize an empty set called seen_numbers
        seen_numbers = set() 

        #For each number in nums
        for num in nums:
            #If the number is already in the set, it's a duplicate
            if num in seen_numbers:
                return True
            #Otherwise add the number to the set
            seen_numbers.add(num) #if initialized to an empty array instead of a set, use append

        # If we've gone through the entire list without finding a duplicate
        return False