class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n+1):
            dp[i] = dp[i-2] + dp[i-1]
            
        return dp[n]
# Time complexity: O(n) Space complexity: O(n)

# Decision tree
#         0
#        / \
#       1   2
#      / \   \
#     2   3   3
#    /     
#   3      
# Here's how to interpret this tree for n=3:

# From the starting position, you have two choices: you can climb 1 step or 2 steps.
# If you climb 1 step (left subtree from root), you can again choose to climb 1 more step (leading you to 2 steps) or 2 steps (leading you to 3 steps).
# If you chose to climb 2 steps from the root (right subtree), then you can only climb 1 more step to reach the 3-step goal.
# The leaves of this tree represent reaching the 3rd step, and there are 3 leaves, which correspond to the 3 distinct ways to climb the staircase.

# This is also a binary tree, so we can use the same approach as we did for the Fibonacci problem: recursion. We can start at the top and work our way down, and we can use memoization to optimize the solution.
# This is a Fibonacci problem in disguise. If we think about the problem statement, we can see that the number of ways to climb n steps is equal to the sum of the number of ways to climb n-1 steps and the number of ways to climb n-2 steps. This is because you can climb 1 step to reach step n-1 from step n-2, or you can climb 2 steps to reach step n-1 from step n-3. This is the same recurrence relation as the Fibonacci sequence, which means that we can use the same dynamic programming approach of memoization to optimize the solution.
# 8, 5, 3, 2, 1, 1 n = 5
# ways(i) = ways(i - 1) + ways(i - 2) where i is the step number on the staircase.