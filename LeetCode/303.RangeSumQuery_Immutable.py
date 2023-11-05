class NumArray:

    def __init__(self, nums: List[int]):
        # Implement the NumArray class
        # Initialize the object with the integer array nums
        self.nums = nums
        
    def sumRange(self, left: int, right: int) -> int:
        # Return the sum of the elements of the nums array in the range [left, right] inclusive
        return sum(self.nums[left:right+1])

# Time: O(n) for the init function, O(1) for the sumRange function
# Space: O(n) for the init function, O(1) for the sumRange function    
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)