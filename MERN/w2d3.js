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
    
    /* Print remaining elements of
    the larger array */
    
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
