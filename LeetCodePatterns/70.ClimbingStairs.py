# https://leetcode.com/problems/climbing-stairs/description/
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        # Initialize base cases
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        
        # Bottom up approach to fill in the dp array
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
    # Time Complexity: O(n)
    # Space Complexity: O(n)   
    # Note: This is a Fibonacci sequence