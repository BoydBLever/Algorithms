* 
  Given an arr and a separator string, output a string of every item in the array separated by the separator.
  No trailing separator at the end.
  Default the separator to a comma with a space after it if no separator is provided.
*/

//1
const arr1 = [1, 2, 3];
const separator1 = ", ";
const expected1 = "1, 2, 3";

const arr2 = [1, 2, 3];
const separator2 = "-";
const expected2 = "1-2-3";

const arr3 = [1, 2, 3];
const separator3 = " - ";
const expected3 = "1 - 2 - 3";

const arr4 = [1];
const separator4 = ", ";
const expected4 = "1";

const arr5 = [];
const separator5 = ", ";
const expected5 = "";

const arr6 = [1, 2, 3];
const separator6 = " and ";
const expected6 = "1 and 2 and 3";

/**
 * Converts the given array into a string of items separated by the given separator.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string|number|boolean>} arr The items to be joined as a string.
 * @param {string} separator To separate each item of the given arr.
 * @returns {string} The given array items as a string separated by the given separator.
 */
//Brandon's solution
function join(arr, separator) {
    var newStr = "";
    for (var i=0; i<arr.length; i++){
        newStr += arr[i];
        if(i != arr.length-1){
            newStr+=separator;
        }
    }
    return newStr;
}
console.log(join(arr1, separator1));
console.log(join(arr2, separator2));
console.log(join(arr3, separator3));
console.log(join(arr4, separator4));
console.log(join(arr5, separator5));
console.log(join(arr6, separator6));

/* 
Book Index
Given an array of ints representing page numbers
return a string with the page numbers formatted as page ranges when the nums
span a consecutive range.
*/

const nums1 = [1, 13, 14, 15, 37, 38, 70];
const expected1 = "1, 13-15, 37-38, 70";

const nums2 = [5, 6, 7, 8, 9];
const expected2 = "5-9";

const nums3 = [1, 2, 3, 7, 9, 15, 16, 17];
const expected3 = "1-3, 7, 9, 15-17";

/**
 * Turns the given arr of page numbers into a string of comma hyphenated
 * page ranges.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums Page numbers.
 * @returns {string} The given page numbers as comma separated hyphenated
 *    page ranges.
 */


function bookIndex(nums) {
    let newString = "";
    let startRange = false;

    // Loop through array
    for(i = 0; i < nums.length; i++){

        //Start of range
        if (i+1 < nums.length && nums[i+1] == nums[i]+1 && startRange == false){
            newString += nums[i] + "-";
            startRange = true;
        }

        //Middle of range
        else if(i+1 < nums.length && nums[i+1] == nums[i]+1 && startRange == true) {
            // Do Nothing
        }

        //End of range
        else if(i+1 < nums.length && nums[i+1] != nums[i]+1 && startRange == true) {
            newString += nums[i] + ", ";
            startRange = false;
        }

        //Not last value in arr
        else if(i+1 < nums.length){
            newString += nums[i] + ", ";
        }

        //Last value in arr
        else{
            newString+= nums[i];
        }
    }
    return newString;
}

function bookIndex(nums) {
    newStr = "";
    for(i=0; i < nums.length; i++){
        newStr += nums[i];
        if(nums[i] == nums[i + 1] - 1){
            while(nums[i] == nums[i+1] - 1){
                i++;
            }
            newStr += ("-" + nums[i])
        }
        if(nums[i] == nums[nums.length - 1]){
            break
        }
        if(nums[i] != nums[i + 1] - 1){
            newStr += ","
        }
    }
    return newStr
}

console.log(bookIndex(nums1, expected1))

console.log(bookIndex(nums2, expected2))

console.log(bookIndex(nums3, expected3))