//Recursion/Backtracking
// https://leetcode.com/problems/subsets-ii/submissions/898653197/?envType=study-plan&id=algorithm-ii
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsetsWithDup = function(nums) {
    nums.sort((a, b) => a - b); // Sort input array to group duplicates together
    const subsets = [];
    const n = nums.length;
    
    const backtrack = (start, subset) => {
        subsets.push(subset);
        for (let i = start; i < n; i++) {
            if (i > start && nums[i] === nums[i-1]) continue; // Skip duplicates
            backtrack(i+1, subset.concat(nums[i]));
        }
    };
    
    backtrack(0, []);
    return subsets;
};