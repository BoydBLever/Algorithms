//Intersect Sorted Arrays
//Given two sorted arrays, return a new array containing all the numbers they have in common

//Ex: given [2,4,7,9,10] and [2,3,5,7,9,10], return [2,7,9,10]
//Ex: given [1,1,4,5,8] and [1,1,1,5,6,8] return [1,1,5,8]
//Ex: given [1,3,5,7,9] and [2,4,6,8,10] return []

// const intersect = (arr1, arr2) => {
//     let m = arr1[arr1.length - 1];
//     let n = arr2[arr2.length - 1];

//     let ans = 0;

//     if (m > n){
//         ans = m;
//     } else {
//         ans = n;
//     }
//     let newtable = Array(ans+1).fill(0);
//     // console.log(arr1[0] + "");

//     newtable[arr1[0]+=1];

//     for (let i = 1; i < arr1.length; i++){
//         if (arr1[i] != arr1[i-1]){
//             console.log(arr1[i] + "");
//             newtable[arr1[i]] += 1;
//         }
//     }

//     for (let j = 0; j < arr2.length; j++){
//         if (newtable[arr2[j]] == 0){
//             console.log(arr2[j] + "");
//             ++newtable[arr2[j]];
//         }
//     }
//     return newtable;
// }

const intersect = (arrLeft, arrRight) => {
    let i = 0;
    let j = 0;
    let outArr = [];

    while (i < arrLeft.length && j < arrRight.length){
        if (arrLeft[i] < arrRight[j]){
            i++;
        }
        if (arrRight[j] < arrLeft[i]){
            j++;
        }
        if (arrLeft[i] === arrRight[j]){
            outArr.push(arrLeft[i]);
            i++;
            j++;
        }
    }

    return outArr;
}

// console.log(intersect([2,4,7,9,10],[2,3,5,7,9,10]));
// console.log(intersect([1,1,4,5,8],[1,1,1,5,6,8]));
// console.log(intersect([1,3,5,7,9],[2,4,6,8,10]));

console.log(intersect([-9, 1, 3, 4, 4, 4, 4, 4, 4, 5, 7], [-5, 0, 1, 1, 1, 1, 1, 2, 4, 4, 6, 7]));

// let arr1 = [1,2,2,2,3];
// let arr2 = [2,3,4,5];
// console.log(intersect([1,2,2,2,3], [2,3,4,5]));