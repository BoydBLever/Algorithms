// https://leetcode.com/problems/decode-ways/submissions/901357100/?envType=study-plan&id=algorithm-ii
/**
 * @param {string} s
 * @return {number}
 */
var numDecodings = function (s) {
    const n = s.length;
    if (s[0] === '0') return 0;
    let dp = Array(n + 1).fill(0);
    dp[0] = 1;
    dp[1] = 1;

    for (let i = 2; i <= n; i++) {
        if (s[i - 1] !== '0') {
            dp[i] += dp[i - 1];
        }
        if (s[i - 2] === '1' || (s[i - 2] === '2' && s[i - 1] <= '6')) {
            dp[i] += dp[i - 2];
        }
    }

    return dp[n];
};