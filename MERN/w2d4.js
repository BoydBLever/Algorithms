
// Finds the most frequent element in an array
function mostFrequent(arr, n) {

    let maxcount = 0;
    let max_freq;
    for (let i = 0; i < n; i++) {
        let count = 0;
        for (let j = 0; j < n; j++) {
            if (arr[i] == arr[j])
                count++;
        }

        if (count > maxcount) {
            maxcount = count;
            max_freq = arr[i];
        }
    }

    return max_freq;
}

let arr = [40, 50, 30, 40, 50, 30, 30];
let n = arr.length;
console.log(mostFrequent(arr, n));
//===================================
/*
*   Write a function that accepts an array of numbers
*   and returns an array of the number(s) that occur
*   the most.
*/
// const mostFrequent = (nums) => {
//     const newArr = [];
//     const map = {};

//     for (let i = 0; i < nums.length; i++) {
//         !map[nums[i]] ? map[nums[i]] = 1 : map[nums[i]]++
//     }
//     const maxValue = Math.max(...Object.values(map));
//     for (key in map) {
//         if (map[key] === maxValue) {
//             newArr.push(parseInt(key));
//         }
//     }
//     return newArr;
// }
// // should return [0]
// console.log(mostFrequent([0, 0, 0, 2, 2, 3]));

// // should return [0,1,2,3,4,5]
// console.log(mostFrequent([0, 1, 2, 3, 4, 5]));

// // should return [5,2]
// console.log(mostFrequent([5, 8, 2, 4, 0, 15, 16, 90, 5, 1, 5, 23, 42, 0, 6, 2, 8, 2, 5, 2]));


// //===================================
// Harder Version
/*
* Returns the k most frequently occurring numbers from the given unordered
* nums array. Order in the return array should be highest frequecy first, 
* ordered to lowest frequency. If two or more numbers match frequency, the
* order they appear in the array does not matter.
*/

// const kMostFrequent = (nums, k) => {
//     const kMostFrequent = (nums, k) => {
//         const newArr = [];
//         const map = {};

//         for (let i = 0; i < nums.length; i++) {
//             !map[nums[i]] ? map[nums[i]] = 1 : map[nums[i]]++
//         }
//         let maxValue = Math.max(...Object.values(map));
//         while (k > 0) {
//             for (key in map) {
//                 if (map[key] === maxValue) {
//                     newArr.push(parseInt(key));
//                     k--;
//                 }
//             }
//             maxValue--;
//         }
//         return newArr;
//     }
// }

// const nums1 = [1, 1, 1, 2, 2, 3];
// const k1 = 2;
// console.log(kMostFrequent(nums1, k1));
// // const expected1 = [1, 2];
// // Explanation: return the two most frequent elements, 1 and 2 are the two most frequent elements

// const nums2 = [0, 0, 0, 2, 2, 3];
// const k2 = 1;
// console.log(kMostFrequent(nums2, k2));
// // const expected2 = [0];
// // Explanation: k being 1 means return the single most frequent element

// const nums3 = [1, 1, 2, 2, 3, 3];
// const k3 = 3;
// console.log(kMostFrequent(nums3, k3));
// // const expected3 = [1, 2, 3];

// const nums4 = [5, 8, 2, 4, 0, 15, 16, 90, 5, 1, 5, 23, 42, 0, 6, 2, 8, 2, 5];
// const k4 = 4;
// console.log(kMostFrequent(nums4, k4));
// // const expected3 = [5, 2, 0, 8];

//=============An object is a natural fit to solve an algorithm
// const mostFrequent = (nums) => {
//     let count = {}
//     let maxCount = 0
//     let maxNum = [nums[0]]
//     for( let i = 0; i < nums.length; i++){
//         //if we haven't counted number yet, make a new entry
//         if(count[nums[i]] === undefined){
//             count[nums[i]] = 1
//         }  else count[nums[i]] += 1
//         //if we find a number with a higher count than maxCount,\
//         //emtpy the maxNum array and start over w that number
//         if(count[nums[i]] > maxCount){
//             maxCount = count[nums[i]]
//             maxNum = [nums[i]]
//         }
//         //if we find a number with the same count, 
//         //add it to max array 
//         else if(count[nums[i]] == maxCount){
//             maxNum.push(nums[i])
//         }
//     } return maxNum
// }
// // should return [0]
// console.log(mostFrequent([0, 0, 0, 2, 2, 3]));

// // should return [0,1,2,3,4,5]
// console.log(mostFrequent([0, 1, 2, 3, 4, 5]));

// // should return [5,2]
// console.log(mostFrequent([5, 8, 2, 4, 0, 15, 16, 90, 5, 1, 5, 23, 42, 0, 6, 2, 8, 2, 5, 2]));

//John Ross posted
// const mostFrequent = (nums) => {
//     let highestVal;
//     let arr = []
//     let count = {}
//     for (let i = 0; i < nums.length; i++) {
//         if (count[nums[i]]) {
//             count[nums[i]] += 1
//         } else {
//             count[nums[i]] = 1
//         }
//     }
//     for (let key in count) {
//         if (count[key] >= highestVal || highestVal == null) {
//             if (count[key] === highestVal) {
//                 arr.push(key)
//             } else {
//                 highestVal = count[key]
//                 arr = [key]
//             }
//         }
//     }
//     return arr
// }

// console.log(mostFrequent([0, 0, 0, 2, 3]))
// console.log(mostFrequent([0, 1, 2, 3, 4, 5]))
// console.log(mostFrequent([5, 8, 2, 4, 0, 15, 16, 90, 5, 1, 5, 23, 42, 0, 6, 2, 8, 2, 5, 2]))