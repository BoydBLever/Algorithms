class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        hset1 = set(nums1)
        hset2 = set(nums2)
        for num in hset1:
            if num in hset2:
                result.append(num)
        return result
# Time complexity: O(n)
# Space complexity: O(n)