/* 
  Acronyms
  Create a function that, given a string, returns the string’s acronym 
  (first letter of each word capitalized). 
  Do it with .split first if you need to, then try to do it without
*/

// const str1 = "object oriented programming";
// const expected1 = "OOP";

// // The 4 pillars of OOP
// const str2 = "abstraction polymorphism inheritance encapsulation";
// const expected2 = "APIE";

// const str3 = "software development life cycle";
// const expected3 = "SDLC";

// // Bonus: ignore extra spaces
// const str4 = "  global   information tracker    ";
// const expected4 = "GIT";

// /**
//  * Turns the given str into an acronym.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {string} wordsStr A string to be turned into an acronym.
//  * @returns {string} The acronym.
//  */

// Solution with split. Does not account for consecutive spaces.
function acronymize(str) {
    const words = str.split(" ")
    acronyms = ""
    for (i=0; i< words.length; i++) {  
        acronyms += words[i][0] //add first letter of each word to acronyms
    }
    return acronyms.toUpperCase()
}
// solution without split. Accounts for consecutive spaces.
function acronymize(str) {
    var acron = "";
    var newStr = "";

    newStr= str;

    //use a for loop to convert using ASCII instead to avoid built in function
    newStr = newStr.toUpperCase();

    for(i=0; i<newStr.length; i++){
        //if the position is zero or the current index is a space && the next iterator is within bounds && the next iterator is not a space
        if ((i == 0 || newStr[i] == " ") && i+1<newStr.length && (newStr[i+1] != " ")) {

            //if the position is 0 and not a space, add the current character to the acron
            if(i == 0 && newStr[i] != " "){
                acron += newStr[i];
            }

            //if the current position is a space and the next isn't, add the next letter to acron
            else{
                acron += newStr[i+1];
            }
        }
    }

    return acron;
}

// console.log(acronymize(str1))
// console.log(acronymize(str2))
// console.log(acronymize(str3))
// console.log(acronymize(str4))


/* 
  String: Is Palindrome
  Create a function that returns a boolean whether the string is a strict palindrome. 
    - palindrome = string that is same forwards and backwards
  
  Do not ignore spaces, punctuation and capitalization
 */

  const str1 = "a x a";
  const expected1 = true;
  
  const str2 = "racecar";
  const expected2 = true;
  
  const str3 = "Dud";
  const expected3 = false;
  
  const str4 = "oho!";
  const expected4 = false;
  
  /**
   * Determines if the given str is a palindrome (same forwards and backwards).
   * - Time: O(?).
   * - Space: O(?).
   * @param {string} str
   * @returns {boolean} Whether the given str is a palindrome or not.
   */

  function isPal(str) {
    for(var left=0; left<str.length/2; left++) { 
        var right = str.length-1-left;           
        if(str[left] != str[right]) {            
            return "Not a pal-indrome!";         
        }
    } return "Pal-indrome!";                     
}

// function isPalindrome(str) {
//     reverseStr = "";
//     for(i=str.length-1; i>=0;i--){
//         reverseStr += str[i];
//     }
//     console.log(reverseStr);
//     if(str == reverseStr){
//         return true;
//     }
//     else{
//         return false;
//     }
// }

