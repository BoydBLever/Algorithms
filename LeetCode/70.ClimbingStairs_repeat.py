class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        
        return dp[n]
    # Time: O(n)
    # Space: O(n)
    # Explanation: dp[i] = dp[i-2] + dp[i-1]
    # dp[i] means the number of ways to climb to i-th step
    # dp[i-2] means the number of ways to climb to i-th step from i-2-th step
    # dp[i-1] means the number of ways to climb to i-th step from i-1-th step
    # So dp[i] = dp[i-2] + dp[i-1]
    # dp[1] = 1, dp[2] = 2, dp[3] = 3, dp[4] = 5, dp[5] = 8, dp[6] = 13, dp[7] = 21, dp[8] = 34, dp[9] = 55, dp[10] = 89
    