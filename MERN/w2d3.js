function returnSortedWithoutIntersection(arr1, arr2, m, n) {
    
    let i = 0, j = 0;
    while (i < m && j < n) {
        if (arr1[i] < arr2[j])
        console.log(arr1[i++] + " ");
        else if (arr2[j] < arr1[i])
        console.log(arr2[j++] + " ");
        else {
            console.log(arr2[j++] + " ");
            i++;
        }
    }
    
    while (i < m)
    console.log(arr1[i++] + " ");
    while (j < n)
    console.log(arr2[j++] + " ");
    return 0;
}

let arr1 = [1, 2, 4, 5, 6];
let arr2 = [2, 3, 5, 7];

let m = arr1.length;
let n = arr2.length;

returnSortedWithoutIntersection(arr1, arr2, m, n);

// function returnSortedWithoutIntersection(arr3, arr4, o, b) {
    
//     let i = 0, j = 0;
//     while (i < o && j < b) {
//         if (arr3[i] < arr4[j])
//         console.log(arr3[i++] + " ");
//         else if (arr4[j] < arr3[i])
//         console.log(arr4[j++] + " ");
//         else {
//             console.log(arr4[j++] + " ");
//             i++;
//         }
//     }
    
//     while (i < o)
//     console.log(arr3[i++] + " ");
//     while (j < b)
//     console.log(arr4[j++] + " ");
//     return 0;
// }

// let arr3 = [1,2,3,4,5];
// let arr4 = [1,6,7,4,8,9];
// let o = arr3.length;
// let b = arr4.length;
// console.log("===============");
// returnSortedWithoutIntersection(arr3, arr4, o, b);