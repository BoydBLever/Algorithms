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
//     const maxValue = Math.max(Object.values(map));
// }

// // should return [0]
// console.log(mostFrequent([0, 0, 0, 2, 2, 3]));

// // should return [0,1,2,3,4,5]
// console.log(mostFrequent([0, 1, 2, 3, 4, 5]));

// // should return [5,2]
// console.log(mostFrequent([5, 8, 2, 4, 0, 15, 16, 90, 5, 1, 5, 23, 42, 0, 6, 2, 8, 2, 5, 2]));

// JavaScript program to find the most frequent element in an array
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