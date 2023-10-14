// https://leetcode.com/problems/jump-game/submissions/900530362/?envType=study-plan&id=algorithm-ii
// To solve this problem, we can use a greedy approach. We can start from the first index and keep track of the farthest index we can reach from that index. For each index, we can update the farthest index using the formula:

// css
// Copy code
// farthestIndex = Math.max(farthestIndex, i + nums[i])
// This means we can reach any index up to farthestIndex from the current index. If at any point, farthestIndex becomes greater than or equal to the last index of the array, we can reach the last index and we can return true. If we have traversed the entire array and farthestIndex is still less than the last index, we cannot reach the last index and we can return false.


var canJump = function(nums) {
    let farthestIndex = 0;
    for (let i = 0; i < nums.length; i++) {
        if (farthestIndex < i) {
            // we cannot reach this index from the previous indices
            return false;
        }
        farthestIndex = Math.max(farthestIndex, i + nums[i]);
        if (farthestIndex >= nums.length - 1) {
            // we can reach the last index
            return true;
        }
    }
    // we have traversed the entire array and cannot reach the last index
    return false;
};

// The canJump function takes an array nums as input and returns true if we can reach the last index of the array or false otherwise. It initializes a variable farthestIndex to 0 and uses a loop to iterate over the array. For each index, it first checks if we can reach this index from the previous indices. If not, we cannot reach the last index and we can return false. Otherwise, it updates farthestIndex using the formula mentioned above. If farthestIndex is greater than or equal to the last index of the array, we can reach the last index and we can return true. Finally, if we have traversed the entire array and farthestIndex is still less than the last index, we cannot reach the last index and we can return false.