#Description: https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/description/
from typing import List

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        count = [0] * 32
        res = 0
        cur = 0
        mod = 1000000007
        
        # Calculate the count of set bits for all numbers
        for num in nums:
            for i in range(32):
                if (num & (1 << i)) != 0:
                    count[i] += 1
        
        for j in range(k):
            cur = 0
            for i in range(32):
                if count[i] > 0:
                    count[i] -= 1
                    cur += 1 << i
            res = (res + cur * cur) % mod
        
        return res