var longestCommonSubsequence = function(text1, text2) {
    const n1 = text1.length, n2 = text2.length;
    const dp = new Array(n2 + 1).fill(0);
    let prev;
    for (let i = 1; i <= n1; i++) {
        prev = dp[0];
        for (let j = 1; j <= n2; j++) {
            let temp = dp[j];
            if (text1[i - 1] === text2[j - 1]) {
                dp[j] = prev + 1;
            } else {
                dp[j] = Math.max(dp[j], dp[j - 1]);
            }
            prev = temp;
        }
    }
    return dp[n2];
};

https://leetcode.com/problems/longest-common-subsequence/submissions/903064321/?envType=study-plan&id=algorithm-ii

//This solution only creates a single row of the dp table and reuses it for each iteration. It also uses two variables prev and temp to keep track of the previous values of the dp table so that we don't need to store the entire table in memory. This reduces the space complexity of the solution to O(n2).