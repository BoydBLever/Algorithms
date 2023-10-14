//Recursion / Backtracking
// https://leetcode.com/problems/subsets/submissions/898649481/?envType=study-plan&id=algorithm-ii
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    const res = [];
    const n = nums.length;
    
    const backtrack = (start, curr) => {
        res.push(curr);
        for (let i = start; i < n; i++) {
            backtrack(i+1, curr.concat(nums[i]));
        }
    };
    
    backtrack(0, []);
    return res;
};
