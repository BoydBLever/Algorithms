// https://leetcode.com/study-plan/algorithm/?progress=x3e584dm
var generateParenthesis = function(n) {
    const combinations = [];
    const generate = (current, open, close) => {
        if (current.length === n * 2) {
            combinations.push(current);
            return;
        }
        if (open < n) {
            generate(current + '(', open + 1, close);
        }
        if (close < open) {
            generate(current + ')', open, close + 1);
        }
    };
    generate('', 0, 0);
    return combinations;
};
