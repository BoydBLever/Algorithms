// https://leetcode.com/problems/number-of-zero-filled-subarrays/description/
var zeroFilledSubarray = function(nums) {
    let count = 0;
    let zeros = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 0) {
            zeros++;
        } else {
            count += (zeros * (zeros + 1)) / 2;
            zeros = 0;
        }
    }
    count += (zeros * (zeros + 1)) / 2;
    return count;
};
