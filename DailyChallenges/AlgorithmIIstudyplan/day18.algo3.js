var integerBreak = function(n) {
    const dp = new Array(n + 1).fill(0);
    dp[1] = 1;
    
    for (let i = 2; i <= n; i++) {
      for (let j = 1; j < i; j++) {
        dp[i] = Math.max(dp[i], j * (i - j), j * dp[i - j]);
      }
    }
    
    return dp[n];
  };
//   https://leetcode.com/problems/integer-break/submissions/903303178/?envType=study-plan&id=algorithm-ii
// Explanation:

// The DP table dp[i] represents the maximum product of breaking the integer i into two or more positive integers.
// The base case is dp[1] = 1, because we cannot break 1 into two or more positive integers.
// To fill in the rest of the DP table, we iterate over all integers i from 2 to n, and over all possible values of the first positive integer j from 1 to i - 1.
// We can either break i into two positive integers j and i - j, or into more than two positive integers, where the first positive integer is j and the remaining positive integers are broken down from i - j. We take the maximum of the two possibilities, and set dp[i] to that value.
// Finally, the result is dp[n].
// This solution has a time complexity of O(n^2), where n is the input integer, and a space complexity of O(n).