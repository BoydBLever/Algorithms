from typing import List
class Solution:

    class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            num_map = {}
            
            for i, num in enumerate(nums):
                complement = target - num
                if complement in num_map:
                    return [num_map[complement], i]
                # Store the index of the number at the end of the loop to avoid using the same number twice
                num_map[num] = i
            
            return []
# Time Complexity: O(n) where n is the number of elements in the array
# Space Complexity: O(n)