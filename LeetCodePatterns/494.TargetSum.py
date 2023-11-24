class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def backtrack(index, current_sum):
            # Base case: if we've gone through all numbers
            if index == len(nums):
                return 1 if current_sum == target else 0
            
            # Include the current number with a '+' sign
            count = backtrack(index + 1, current_sum + nums[index])
            
            # Include the current number with a '-' sign
            count += backtrack(index + 1, current_sum - nums[index])
            
            return count

        return backtrack(0, 0)
# Decision Tree for nums = [1, 2], target = 1
#                      [0]  (Starting Sum)
#                 ______|______
#                /             \
#              [1]            [-1]   (Adding/Subtracting 1)
#             /   \           /   \
#           [3]   [-1]      [1]   [-3]  (Adding/Subtracting 2)
