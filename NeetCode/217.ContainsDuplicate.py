# https://leetcode.com/problems/contains-duplicate/
# HashSet contains unique elements and HashMap, HashTable contains unique keys.
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #Solution 1
        # return len(nums) != len(set(nums))

        #Solution 2
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
#time complexity: O(n)
#space complexity: O(n)
    
#test processing function
if __name__ == '__main__':
    nums = [1,2,3,1]
    print(Solution().containsDuplicate(nums))
    nums = [1,2,3,4]
    print(Solution().containsDuplicate(nums))

#test result
'''
True
False
'''