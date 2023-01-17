//Intersect Sorted Arrays
//Given two sorted arrays, return a new array containing all the numbers they have in common

//Ex: given [2,4,7,9,10] and [2,3,5,7,9,10], return [2,7,9,10]
//Ex: given [1,1,4,5,8] and [1,1,1,5,6,8] return [1,1,5,8]
//Ex: given [1,3,5,7,9] and [2,4,6,8,10] return []

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

console.log(intersect([-9, 1, 3, 4, 4, 4, 4, 4, 4, 5, 7], [-5, 0, 1, 1, 1, 1, 1, 2, 4, 4, 6, 7]));