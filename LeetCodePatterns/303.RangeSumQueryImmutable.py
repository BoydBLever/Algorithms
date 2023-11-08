class NumArray:

    def __init__(self, nums: List[int]):
        # self.nums = nums
        self.cumulative_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):  # Starting from 0 up to len(nums)-1
            self.cumulative_sum[i + 1] = self.cumulative_sum[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        # return sum(self.nums[left:right +1])
        return self.cumulative_sum[right + 1] - self.cumulative_sum[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)