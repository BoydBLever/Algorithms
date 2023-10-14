// https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/900162624/?envType=study-plan&id=algorithm-ii
/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    const mappings = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    };
    const combinations = [];
    if (digits.length === 0) {
        return combinations;
    }
    const generateCombinations = (current, index) => {
        if (index === digits.length) {
            combinations.push(current);
            return;
        }
        const letters = mappings[digits[index]];
        for (let i = 0; i < letters.length; i++) {
            generateCombinations(current + letters[i], index + 1);
        }
    };
    generateCombinations('', 0);
    return combinations;
};