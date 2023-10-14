# https://leetcode.com/problems/longest-consecutive-sequence/
from typing import List

class Solution:
    def longestConsecutive(self, nums):
        # Convert the list of numbers to a set for O(1) lookup
        nums_set = set(nums)
        
        # Initialize the maximum sequence length to 0
        longest_sequence = 0
        
        # Iterate over each number in the set
        for num in nums_set:
            # Check if the number is the start of a sequence
            if num - 1 not in nums_set:
                # Start with the current number and a sequence length of 1
                current_num = num
                current_sequence = 1
                
                # Check the next numbers in the sequence
                while current_num + 1 in nums_set:
                    current_num += 1
                    current_sequence += 1
                
                # Update the maximum sequence length if needed
                longest_sequence = max(longest_sequence, current_sequence)
        
        # Return the longest consecutive sequence length
        return longest_sequence
    
    #NeetCode solution
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     numSet = set(nums)
    #     longest = 0

    #     for n in nums:
    #         #check if its the start of a sequence
    #         if (n - 1) not in numSet:
    #             length = 0
    #             while (n + length) in numSet:
    #                 length += 1
    #             longest = max(length, longest)
    #     return longest