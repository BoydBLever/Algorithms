//Recursion/Backtracking
//https://leetcode.com/problems/combination-sum-ii/description/?envType=study-plan&id=algorithm-ii
/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum2 = function(candidates, target) {
    candidates.sort((a, b) => a - b); // Sort input array to group duplicates together
    const combinations = [];
    const n = candidates.length;
    const used = new Array(n).fill(false); // Initialize boolean array of used elements
    
    const backtrack = (start, curr, remain) => {
        if (remain === 0) {
            combinations.push(curr);
        } else if (remain > 0) {
            for (let i = start; i < n; i++) {
                if (used[i] || (i > start && candidates[i] === candidates[i-1] && !used[i-1])) continue; // Skip duplicates
                used[i] = true;
                backtrack(i+1, curr.concat(candidates[i]), remain - candidates[i]);
                used[i] = false;
            }
        }
    };
    
    backtrack(0, [], target);
    return combinations;
};