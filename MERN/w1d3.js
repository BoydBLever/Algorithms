// combine two pre-sorted arrays into one sorted array
// return the newly combined array
// bonus challenge: combine in place into LeftArr instead of a new array
// const combine = (leftArr, rightArr) => {
//     for (let i = 0; i < rightArr.length; i++) {
//         leftArr.push(rightArr[i]);
//     }
//     return leftArr;
// }
const combine = (leftArr, rightArr) => {
    let left = 0;
    let right = 0;
    let newArr = []
    
    while (left < leftArr.length && right < rightArr.length) {
        if (leftArr[left] < rightArr[right]) {
            newArr.push(leftArr[left]);
            left++;
        }
        else {
            newArr.push(rightArr[right]);
            right++;
        }
    }
    while (right < rightArr.length) {
        newArr.push(rightArr[right]);
        right++;
    }
    while (left < leftArr.length) {
        newArr.push(leftArr[left]);
        left++;
    }
    return newArr;
}
// should return [1,2,3,4,5,6,7]
console.log(combine([1, 2, 3, 4, 5], [6, 7]));
// should return [78]
console.log(combine([78], []));
// should return []
console.log(combine([], []));
// should return [0,1,2,3,7,9,11,15,109]
console.log(combine([3, 9, 10], [0, 1, 2, 7, 11, 15, 109]));
