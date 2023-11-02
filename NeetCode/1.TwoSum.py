# https://leetcode.com/problems/two-sum/

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Solution 1
        # hashset = set()
        # for i in range(len(nums)):
        #     if target - nums[i] in hashset:
        #         return [nums.index(target - nums[i]), i]
        #     hashset.add(nums[i])
        # return []
        #time complexity: O(n)
        #space complexity: O(n)

        #Solution 2
        hashmap = {}
        for i in range(len(nums)):
            if target - nums[i] in hashmap:
                return [hashmap[target - nums[i]], i]
            hashmap[nums[i]] = i
        return []
        #time complexity: O(n)
        #space complexity: O(n)

        # Solution 3 - NeetCode
        # prevMap = {} # val : index
        # for i, n in enumerate(nums):
        #     diff = target - n 
        #     if diff in prevMap:
        #         return [prevMap[diff], i]
        #     prevMap[n] = i
        # return []

#test processing function
if __name__ == '__main__':
    nums = [2,7,11,15] 
    target = 9
    print(Solution().twoSum(nums, target)) # [0, 1]
    nums = [3,2,4]
    target = 6
    print(Solution().twoSum(nums, target)) # [1, 2]
    nums = [3,3]
    target = 6
    print(Solution().twoSum(nums, target)) # [0, 1]