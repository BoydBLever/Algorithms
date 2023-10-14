// https://leetcode.com/problems/arithmetic-slices/submissions/901353783/?envType=study-plan&id=algorithm-ii
/**
 * @param {number[]} nums
 * @return {number}
 */
var numberOfArithmeticSlices = function (nums) {
    const n = nums.length;
    let dp = Array(n).fill(0);
    let count = 0;

    for (let i = 2; i < n; i++) {
        if (nums[i] - nums[i - 1] === nums[i - 1] - nums[i - 2]) {
            dp[i] = dp[i - 1] + 1;
            count += dp[i];
        }
    }

    return count;
};