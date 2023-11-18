class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0  # Initialize the left pointer
        right = 0  # Initialize the right pointer

        # Iterate through the list
        while right < len(nums):
            # If the current element is non-zero
            if nums[right] != 0:
                # Swap the current element with the element at the left pointer
                nums[left], nums[right] = nums[right], nums[left]
                # Move the left pointer to the next position
                left += 1
            # Move the right pointer to the next position
            right += 1