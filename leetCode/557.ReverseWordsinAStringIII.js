// Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

// Example 1:

// Input: s = "Let's take LeetCode contest"
// Output: "s'teL ekat edoCteeL tsetnoc"
// Example 2:

// Input: s = "God Ding"
// Output: "doG gniD"
 

// Constraints:

// 1 <= s.length <= 5 * 104
// s contains printable ASCII characters.
// s does not contain any leading or trailing spaces.
// There is at least one word in s.
// All the words in s are separated by a single space.
/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    // Split the string by space to get an array of words
    var words = s.split(' ');

    // For each word in the array, reverse the word
    var reversedWords = words.map(word => word.split('').reverse().join(''));

    // Join the reversed words using a space to get the final string
    return reversedWords.join(' ');
};
