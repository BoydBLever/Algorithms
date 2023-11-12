class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort(reverse=True)  # Sort the numbers in descending order
        max_xor = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                # Check if (nums[i], nums[j]) is a strong pair
                if abs(nums[i] - nums[j]) <= nums[j]:
                    max_xor = max(max_xor, nums[i] ^ nums[j])
        return max_xor