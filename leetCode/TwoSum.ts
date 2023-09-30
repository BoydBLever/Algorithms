function twoSum(nums: number[], target: number): number[] {
    let numMap: { [key: number]: number} = {};
    for (let i = 0; i < nums.length; i++) {
        let complement = target - nums[i];
        if (numMap.hasOwnProperty(complement)){
            return [numMap[complement], i];
        }
        numMap[nums[i]] = i;
    }
    return [];
};
