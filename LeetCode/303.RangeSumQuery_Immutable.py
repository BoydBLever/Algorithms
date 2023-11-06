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

# Dynamic Programming solution
# DP becomes more efficient when there is a large number of queries
class NumArray:

    def __init__(self, nums: List[int]):
        # self.nums = nums
        self.cumulative_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):  # Starting from 0 up to len(nums)-1
            self.cumulative_sum[i + 1] = self.cumulative_sum[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        # return sum(self.nums[left:right +1])
        return self.cumulative_sum[right + 1] - self.cumulative_sum[left]
    
#  The fundamental importance of this NumArray solution lies in its preprocessing step, which builds a cumulative sum array. This array enables constant-time queries for the sum of any range within the original array. The sumRange function is implemented by simply subtracting the cumulative sum at the left index from the cumulative sum just after the right index. This is possible because the cumulative sum array is constructed such that each element is the sum of all previous elements in the original array. Thus, the difference between the cumulative sum at the right index and the cumulative sum just before the left index is the sum of all elements between the left and right indices, inclusive.