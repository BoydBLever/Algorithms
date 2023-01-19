
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