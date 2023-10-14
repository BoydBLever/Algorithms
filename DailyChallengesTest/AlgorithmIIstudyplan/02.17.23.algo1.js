// https://leetcode.com/problems/house-robber-ii/submissions/900528608/?envType=study-plan&id=algorithm-ii
var rob = function(nums) {
    if (nums.length === 1) {
        return nums[0];
    }
    
    const robFirst = robHelper(nums.slice(0, nums.length-1));
    const robLast = robHelper(nums.slice(1));
    
    return Math.max(robFirst, robLast);
};

function robHelper(nums) {
    if (nums.length === 1) {
        return nums[0];
    }
    
    let dp = new Array(nums.length);
    dp[0] = nums[0];
    dp[1] = Math.max(nums[0], nums[1]);
    
    for (let i = 2; i < nums.length; i++) {
        dp[i] = Math.max(dp[i-1], dp[i-2] + nums[i]);
    }
    
    return dp[nums.length-1];
}
