//There are two functions and two sets of data here. Comment out one to run the other, and vice versa.
/**
 * Encodes the given string such that duplicate characters appear once followed
 * by a number representing how many times the char occurs. Only encode strings
 * when the result yields a shorter length.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str The string to encode.
 * @returns {string} The given string encoded.
 */

// const str1 = "aaaabbcddd";
// const expected1 = "a4b2c1d3";

// const str2 = "";
// const expected2 = "";

// const str3 = "a";
// const expected3 = "a";

// const str4 = "bbcc";
// const expected4 = "bbcc";


// function findNum(strng){
//     let newStr = '';
//     let sum = 1;
//     for(i=0; i < strng.length; i++){
//         newStr += strng[i];
//         if(strng[i] != strng[i + 1]){
//             newStr += sum;
//         }
//         if(strng[i] == strng[i + 1]){
//             while(strng[i] == strng[i + 1]){
//                 sum += 1;
//                 i++;
//             }
//             newStr += sum;
//             sum = 1;
//         }
//     }
//     if(strng.length <= newStr.length){
//         return strng;
//     }
//     return newStr;
// }

// console.log(findNum(str1))

// console.log(findNum(str2))

// console.log(findNum(str3))

// console.log(findNum(str4))

/* 
String Decode  
*/

const str1 = "a3b2c1d3";
const expected1 = "aaabbcddd";

const str2 = "a3b2c12d10";
const expected2 = "aaabbccccccccccccdddddddddd";

/**
 * Decodes the given string by duplicating each character by the following int
 * amount if there is an int after the character.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str An encoded string with characters that may have an int
 *    after indicating how many times the character occurs.
 * @returns {string} The given str decoded / expanded.
 */
//consider using isNan
//consider using parseInt

//include code here
function decodeStr(str) {
    let newStr = ""
    for (i = 0; i < str.length; i++) {

        if (!isNaN(str[i])) { //NaN stands for not a number. !isNaN will mean it is a number.
            let numString = "" //it doesn't have to be here, but it could appear later. I could put a let on line 91 instead
            let startPos = i

            while (!isNaN(str[i])) {
                i++ //this value appears in line 91, as i.
            }

            numString = str.substring(startPos, i) //substring takes a piece of a string out, from start index (inclusive) to ending index (exclusive)
            loopNum = parseInt(numString) //parseInt turns a string into a number i.e. parseInt("5") == 5
            while (loopNum > 0) {
                newStr += str[startPos - 1] //startPos - 1 is the letter attached to the number (before)
                loopNum--
            }
        }
    }
    return newStr
}
console.log(decodeStr(str1))
console.log(decodeStr(str2))
