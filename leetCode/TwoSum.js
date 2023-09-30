//Strategy
// I solve the Two Sum problem here using a hash map, or an object in JavaScript. The idea is to iterate over the 'nums' array and for each number, calculate its completement with respect to the target. Then, check if this complement is present in the hash map. It it does, then these two numbers add to the target. If not, the current number and its index are stroed in the hash map, and the iteration will move to the next number.

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let numMap = {};
    for (let i = 0; i < nums.length; i++){
        let complement = target - nums[i];
        if (numMap.hasOwnProperty(complement)){
            return [numMap[complement], i];
        }
        numMap[nums[i]] = i;
    }
};
