//Recursion/Backtracking
//https://leetcode.com/problems/combination-sum/description/?envType=study-plan&id=algorithm-ii
/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    const combinations = [];
    const n = candidates.length;
    
    const backtrack = (start, curr, remain) => {
        if (remain === 0) {
            combinations.push(curr);
        } else if (remain > 0) {
            for (let i = start; i < n; i++) {
                if (candidates[i] <= remain) {
                    backtrack(i, curr.concat(candidates[i]), remain - candidates[i]);
                }
            }
        }
    };
    
    backtrack(0, [], target);
    return combinations;
};