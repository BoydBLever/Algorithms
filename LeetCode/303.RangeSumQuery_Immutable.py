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
    
#  The fundamental importance of this NumArray solution lies in its preprocessing step, which builds a cumulative sum array. This array enables constant-time queries for the sum of any range within the original array. It's a classic example of a time-memory trade-off: we spend additional memory to store precomputed sums to save time on repeated sum queries.

# This preprocessing concept can be extended beyond sum queries to other cumulative metrics. For example, if you're dealing with probabilities, products, minima, or maxima, a similar approach could be taken where you preprocess the array in such a way that any segment's metric can be computed quickly. The idea is to spend time upfront to save time later, which is the crux of dynamic programming: breaking down a problem into simpler subproblems, solving each subproblem just once, and storing their solutions—often in an array or matrix—so that they can be reused (or "recalled") to solve larger subproblems.

# In the larger context of dynamic programming, the NumArray class demonstrates the technique of overlapping subproblem optimization. In other problems, such as computing the nth Fibonacci number, the longest common subsequence, or the number of ways to make change for a given amount, the same principle applies. By remembering the solutions to smaller subproblems, you can build up the solution to the problem at hand without redundant calculations. This approach can significantly reduce the time complexity from exponential to polynomial for many problems.