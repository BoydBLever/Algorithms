//Recursion/Backtracking
//https://leetcode.com/problems/permutations-ii/submissions/898657194/?envType=study-plan&id=algorithm-ii
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permuteUnique = function(nums) {
    nums.sort((a, b) => a - b); // Sort input array to group duplicates together
    const permutations = [];
    const n = nums.length;
    const used = new Array(n).fill(false); // Initialize boolean array of used elements
    
    const backtrack = (curr) => {
        if (curr.length === n) {
            permutations.push(curr);
        } else {
            for (let i = 0; i < n; i++) {
                if (used[i] || (i > 0 && nums[i] === nums[i-1] && !used[i-1])) continue; // Skip duplicates
                used[i] = true;
                backtrack(curr.concat(nums[i]));
                used[i] = false;
            }
        }
    };
    
    backtrack([]);
    return permutations;
};