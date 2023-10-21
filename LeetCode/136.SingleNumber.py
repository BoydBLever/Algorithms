# https://leetcode.com/problems/single-number/
# NeetCode solution
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # xored is the key here
        res = 0 # n ^ 0  = n
        for n in nums:
            res = n ^ res
        return res 