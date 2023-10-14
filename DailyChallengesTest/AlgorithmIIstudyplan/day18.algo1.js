var minDistance = function (word1, word2) {
    const m = word1.length;
    const n = word2.length;
    const dp = new Array(m + 1).fill(null).map(() => new Array(n + 1).fill(0));

    // Initialize the first row and column of the DP table.
    for (let i = 0; i <= m; i++) {
        dp[i][0] = i;
    }
    for (let j = 0; j <= n; j++) {
        dp[0][j] = j;
    }

    // Fill in the rest of the DP table.
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            if (word1[i - 1] === word2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1];
            } else {
                dp[i][j] = 1 + Math.min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]);
            }
        }
    }

    return dp[m][n];
};

//   https://leetcode.com/problems/edit-distance/submissions/903291461/?envType=study-plan&id=algorithm-ii
// Explanation:

// The DP table dp[i][j] represents the minimum number of operations required to convert the substring word1[0...i-1] to the substring word2[0...j-1].
// The base case is dp[0][0] = 0, because the empty string requires zero operations to convert to itself.
// To fill in the rest of the DP table, we iterate over all pairs (i, j) in increasing order of i and j.
// If word1[i-1] is equal to word2[j-1], then we don't need to perform any operation, so we set dp[i][j] = dp[i-1][j-1].
// If word1[i-1] is not equal to word2[j-1], then we can either insert, delete, or replace a character to make them equal. We take the minimum of the three possible operations, plus 1, and set dp[i][j] to that value.
// Finally, the result is dp[m][n], where m and n are the lengths of word1 and word2, respectively.
// This solution has a time complexity of O(mn), where m and n are the lengths of the input strings, and a space complexity of O(mn).