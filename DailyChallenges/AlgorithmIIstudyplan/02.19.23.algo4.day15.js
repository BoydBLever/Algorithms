// https://leetcode.com/problems/word-break/submissions/901358162/?envType=study-plan&id=algorithm-ii
var wordBreak = function (s, wordDict) {
    const n = s.length;
    let dp = Array(n + 1).fill(false);
    dp[0] = true;

    for (let i = 1; i <= n; i++) {
        for (let j = 0; j < i; j++) {
            if (dp[j] && wordDict.includes(s.substring(j, i))) {
                dp[i] = true;
                break;
            }
        }
    }

    return dp[n];
};
