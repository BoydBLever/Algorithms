class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] *= -1
        
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
# Time Complexity: O(n)
# Space Complexity: O(1)