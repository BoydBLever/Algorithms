class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Create two arrays for left and right products
        left = [1] * len(nums)
        right = [1] * len(nums)

        # Fill the left array
        for i in range(1, len(nums)):
            # Calculate the product of all elements to the left of i, the current element. For each i, it multiplies the product up to i - 1 with the element at i - 1.
            left[i] = left[i-1] * nums[i-1]
        
        # Fill the right array. Iterate backward from the end of the array. The loop starts from the second-to-last element and goes backwards to the beginning of the array.
        for i in range(len(nums)-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
        
        # Multiply the left and right arrays
        for i in range(len(nums)):
            nums[i] = left[i] * right[i]
        # Return the nums array
        return nums