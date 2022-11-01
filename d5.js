// var fruit1 = "apples";
// var fruit2 = "oranges";

// fruit1 = fruit2;
// fruit2 = fruit1;

// var temp = fruit1;
// fruit1 = fruit2;
// fruit2 = temp;
// //The simplest way to swap two variables.
// //It is very standard.

// console.log("My favorite fruit is " + fruit1);
// console.log("My second favorite fruit is " + fruit2);

//How to think of variables and how to swap them?
//We need a third variable. Call it a temp swap.
//In the above example, var temp is the third variable.

// var start = 0;
// var end = 12;
// while (start < end);{
//     console.log('start: ${start}, end: ${end}'); //string interpolation
//    //back ticks, dollar sign and curly braces with variable name defined inside.
//     start += 2;
//     end -= 2;
// }

function reverse(arr) {
    var start = 0;
    var end = (arr.length - 1)
    while (start < end) {
        var temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        start++;
        end--;
    }
    return arr;
}
var letters = ["a", "b", "c", "d", "e"];
console.log(reverse(letters)); //should print out ["e","d","c","b","a"]