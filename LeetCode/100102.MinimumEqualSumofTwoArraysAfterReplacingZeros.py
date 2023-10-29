# https://leetcode.com/contest/weekly-contest-369/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/

# hululu0405's solution
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = sum(nums1), sum(nums2)
        z1, z2 = nums1.count(0), nums2.count(0)
        if (s1 < s2 + z2 and z1 == 0) or (s1 + z1 > s2 and z2 == 0):
            return -1
        return max(s1+z1, s2+z2)