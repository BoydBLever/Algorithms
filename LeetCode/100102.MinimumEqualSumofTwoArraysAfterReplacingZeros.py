# https://leetcode.com/contest/weekly-contest-369/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/

import heapq

class Solution:
    def minSum(self, nums1: [int], nums2: [int]) -> int:
        sum1, sum2 = sum(nums1), sum(nums2)
        if sum1 > sum2:
            nums1, nums2, sum1, sum2 = nums2, nums1, sum2, sum1  # Make nums1 always the smaller sum
        
        diff = sum2 - sum1

        if diff == 0:
            return sum1 + sum2
        
        # Calculate gains for nums1 and losses for nums2 when replacing 0s
        gains = [-num + 6 if num < 6 else 0 for num in nums1] + [num - 1 for num in nums2 if num > 1]
        heapq.heapify(gains)  # Min heap
        
        operations = 0
        while diff > 0 and gains:
            gain = -heapq.heappop(gains)
            diff -= gain
            operations += 1

        return sum1 + sum2 + operations if diff <= 0 else -1