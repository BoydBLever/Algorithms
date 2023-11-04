class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        for num in nums:
            single ^= num
        return single
    # Time Complexity: O(n)
    # Space Complexity: O(1)