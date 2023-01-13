//partition the array around the value at arr[0]
//without creating a new array
//values left of the original pivot should be less than the pivot
//values right of the pivot should be >= the pivot value
//note: each side of the partitioned value does not
//have to be sorted. some solutions might return slightly
//different results
//return the partitioned array
//bonus: return the index where the value at 0 ends up
//[5,4,9,2,5,3] -> [4,2,3,5,9,5], return 3
const partition = (arr) => {
    let pivi = 0;
    for(var i = 1; i < arr.length; i++){
        if (arr[i] < arr[pivi]){
            console.log(`trying to move ${arr[i]} back`);
            let tempi = i;
            while(tempi > pivi){
                console.log(`swapping ${arr[tempi]} with ${arr[tempi - 1]}`);
                let temp = arr[tempi];
                arr[tempi] = arr[tempi - 1];
                arr[tempi - 1] = temp;
                tempi--;
            }
            pivi++;
            console.log(arr);
        }
    }
    return arr;
}

//should return [4,2,3,5,9,5]
console.log(partition([5,4,9,2,5,3]));
//should return [4,7]
console.log(partition([7,4]));
//should return [2,1,3,4,5]
console.log(partition([3,5,1,2,4]));
//should return [2,1,7,10,15]
console.log(partition([7,2,10,15,1]));