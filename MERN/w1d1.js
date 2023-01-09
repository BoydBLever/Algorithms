function bblSort(arr) {
    for (var i = 0; i < arr.length; i++) {
        // i elements are already in place 
        for (var j = 0; j < (arr.length - i - 1); j++) {
            // Checking if the item at present iteration
            // is greater than the next iteration
            if (arr[j] > arr[j + 1]) {
                // If the condition is true then swap them
                var temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
            }
        }
    }
    // Print the sorted array
    console.log(arr);
}
// This is our unsorted array
var arr1 = [234, 43, 55, 63, 5, 6, 235, 547];
var arr2 = [5, 4, 2, 6, 8, 14];
// Now pass this array to the bblSort() function
bblSort(arr1);
bblSort(arr2);

// FROM W1D1 AM CLASS LECTURE
// Efficiency for how things run: big O. What is the worst case scenario?
function bubbleSort(array){
    let swapped = true;
    while(swapped){
        console.log("running the inner loop again");
        swapped = false;
        for(let i = 0; i < array.length; i++){
            if(array[i] > array[i+1]){
                console.log(`swapping bigger value ${array[i]} with smaller value ${array[i+1]}`);
                let temp = array[i];
                array[i] = array[i+1];
                array[i+1] = temp;
                
                swapped = true;
            }
        }
    }
    return array;
}

var test1 = [5,4,2,6,8,14,1,3,20,-5,24];
console.log(bubbleSort(test1));