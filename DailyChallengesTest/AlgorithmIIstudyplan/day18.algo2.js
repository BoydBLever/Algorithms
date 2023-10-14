var coinChange = function(coins, amount) {
    const dp = new Array(amount + 1).fill(Infinity);
    dp[0] = 0;
    
    for (let i = 1; i <= amount; i++) {
      for (let j = 0; j < coins.length; j++) {
        if (coins[j] <= i) {
          dp[i] = Math.min(dp[i], dp[i - coins[j]] + 1);
        }
      }
    }
    
    return dp[amount] === Infinity ? -1 : dp[amount];
  };

//   Explanation:

//   https://leetcode.com/problems/coin-change/submissions/903297055/?envType=study-plan&id=algorithm-ii
// The DP table dp[i] represents the minimum number of coins required to make up the amount i.
// The base case is dp[0] = 0, because we don't need any coins to make up an amount of zero.
// To fill in the rest of the DP table, we iterate over all amounts i from 1 to amount, and over all coin denominations j from 0 to coins.length - 1.
// If coins[j] <= i, then we can either use the j-th coin or not use it. If we use it, then we subtract coins[j] from the current amount i and add 1 to the result. We take the minimum of the two possibilities, and set dp[i] to that value.
// Finally, the result is dp[amount], if it is less than or equal to amount, and -1 otherwise.
// This solution has a time complexity of O(amount * coins.length), where amount is the target amount and coins.length is the number of coins, and a space complexity of O(amount).