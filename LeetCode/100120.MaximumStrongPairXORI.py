class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        # Time: O(N), Space: O(1)
        # The maximum XOR of two numbers is the XOR of the two numbers with the highest bit difference.
         # Initialize the result
        max_xor = 0
        # Sort the nums array to ensure strong pair condition
        nums.sort()
        # Use a double loop to consider all pairs
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                # Strong pair condition check
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                    # Calculate XOR and update max_xor if necessary
                    max_xor = max(max_xor, nums[i] ^ nums[j])
        return max_xor
