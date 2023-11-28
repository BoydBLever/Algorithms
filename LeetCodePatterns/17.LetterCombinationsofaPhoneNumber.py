# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return res
        part = []
        self.dfs(digits, 0, part, res)
        return res
    
    def dfs(self, digits, i, part, res):
        # base case
        if i >= len(digits):
            res.append("".join(part))
            return
        for c in self.getLetters(digits[i]):
            part.append(c)
            self.dfs(digits, i + 1, part, res)
            part.pop()
    
    def getLetters(self, digit):
        if digit == "2":
            return "abc"
        elif digit == "3":
            return "def"
        elif digit == "4":
            return "ghi"
        elif digit == "5":
            return "jkl"
        elif digit == "6":
            return "mno"
        elif digit == "7":
            return "pqrs"
        elif digit == "8":
            return "tuv"
        elif digit == "9":
            return "wxyz"
        else:
            return ""
    # Time Complexity: O(3^n * 4^m), where n is the number of digits in the input that maps to 3 letters (e.g. 2, 3, 4, 5, 6, 8) and m is the number of digits in the input that maps to 4 letters (e.g. 7, 9), and n + m is the total number digits in the input.
    # Space Complexity: O(3^n * 4^m), since one has to keep 3^n * 4^m solutions.