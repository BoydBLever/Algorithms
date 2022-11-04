/* 
  November 4, 2022
  Given a string that may have extra spaces at the start and the end,
  return a new string that has the extra spaces at the start and the end trimmed (removed)
  do not remove any other spaces.
*/

const str1 = "   hello world     ";
const expected1 = "hello world";

const str2 = "     goodbye     world     "
const expected2 = "goodbye     world"


/**
 * Trims any leading or trailing white space from the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The given string with any leading or trailing white space
 *    stripped.
 */
function trim(str) {
var start;
    var end;
    for(var i = 0; i < str.length; i++){
        if(str[i] != ' '){
            start = i;
            console.log(start)
            break
        }
    }
    for( var j = str.length -1; j >= 0; j--){
        if(str[j] != ' '){
            end = j+1;
            console.log(end)
            break
        }
    }
    return str.slice(start, end)
}

console.log(trim(str2));

/* 
  An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
  typically using all the original letters exactly once.
  Is there a quick way to determine if they aren't an anagram before spending more time?
  Given two strings
  return whether or not they are anagrams
// */

const strA1 = "yes";
const strB1 = "eys";
const expected1 = true;

const strA2 = "yes";
const strB2 = "eYs"; 
const expected2 = true;

const strA3 = "no";
const strB3 = "noo";
const expected3 = false;

const strA4 = "silent";
const strB4 = "listen";
const expected4 = true;

/**
 * Determines whether s1 and s2 are anagrams of each other.
 * Anagrams have all the same letters but in different orders.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} s1
 * @param {string} s2
 * @returns {boolean} Whether s1 and s2 are anagrams.
 */

function isAnagram(s1, s2) {
    //if strings are the same length
    if (s1.length == s2.length){
        s1 = s1.toLowerCase();
        s2 = s2.toLowerCase();

        s1Obj = {};
        s2Obj = {};

        //create key for each letter in s1 and keep track of their quantity
        for (i = 0; i<s1.length; i++){
            //if key already exists, increases by 1
            if (s1[i] in s1Obj){
                s1Obj[s1[i]]++;
            }

            //if key does not exist, create one and set it equal to 1
            else{
                s1Obj[s1[i]]=1;
            }
        }

        //create key for each letter in s2 and keep track of their quantity
        for (i = 0; i<s2.length; i++){
            //if key already exists, increases by 1
            if (s2[i] in s2Obj){
                s2Obj[s2[i]]++;
            }

            //if key does not exist, create one and set it equal to 1
            else{
                s2Obj[s2[i]]=1;
            }
        }
        console.log(s1Obj);
        console.log(s2Obj);

        //for each key in first object
        //compares keys/values to second object
        for (key in s1Obj){
            //check if values at key are equal
            if (s1Obj[key] != s2Obj[key]){
                return false;
            }
        }
        // //for each key in second object
        // //compares keys/values to first object
        // for (key in s2Obj){
        //     //check if values at key are equal
        //     if (s2Obj[key] != s1Obj[key]){
        //         return false;
        //     }
        // }

        return true;
    }

    //if strings are not the same length
    else{
        return false;
    }
}

console.log(isAnagram(strA1, strB1));
console.log(isAnagram(strA2, strB2));
console.log(isAnagram(strA3, strB3));
console.log(isAnagram(strA4, strB4));
/*****************************************************************************/