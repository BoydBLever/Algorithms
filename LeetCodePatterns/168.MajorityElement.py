class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for num in nums:
            if nums.count(num) > len(nums) // 2:
                return num
            # Time: O(n^2) -> this is slow
            # Space: O(1)   

        # Boyer-Moore Voting Algorithm
        # Time: O(n)
        # Space: O(1)
        count = 0
        candidate = None
        
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        
        return candidate