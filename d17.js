/* 
  Given a string containing space separated words
  Reverse each word in the string.
  If you need to, use .split to start, then try to do it without.
*/

const str1 = "hello";
const expected1 = "olleh";

const str2 = "hello world";
const expected2 = "olleh dlrow";

const str3 = "abc def ghi";
const expected3 = "cba fed ihg";

/**
 * Reverses the letters in each words in the given space separated
 * string of words. Does NOT reverse the order of the words themselves.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str Contains space separated words.
 * @returns {string} The given string with each word's letters reversed.
 */

// Solution

function reverseString(string) {
    var tempWord = "";
    var newString = " ";
    for (i = string.length - 1; i >= 0; i--) {
        if (string[i] != " ") {
            tempWord += string[i];
        }
        if (string[i] == " ") {
            newString = tempWord + " " + newString;
            tempWord = " ";
        }
    }
    newString = tempWord + " " + newString;
    return newString;
}
console.log(reverseString(str1));
console.log(reverseString(str2));
console.log(reverseString(str3));

/*
  Reverse Word Order
  Given a string of words (with spaces)
  return a new string with words in reverse sequence.
*/

const str1 = "This is a test";
const expected1 = "test a is This";

const str2 = "hello";
const expected2 = "hello";

const str3 = "   This  is a   test  ";
const expected3 = "test a is This";

/**
 * Reverses the order of the words but not the words themselves form the given
 * string of space separated words.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} wordsStr A string containing space separated words.
 * @returns {string} The given string with the word order reversed but the words
 *    themselves are not reversed.
 */

function reverseWordOrder(wordsStr) {
    let words = wordsStr.split(" ")
    let revWords = []
    for(let i=words.length-1;i>=0;i--){
        if(words[i] != ''){
            revWords.push(words[i])
        }
    }
    return revWords.join(" ")
}
console.log(reverseWordOrder(str3))