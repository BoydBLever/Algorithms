# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         res = []
#         if not digits:
#             return res
#         part = []
#         self.dfs(digits, 0, part, res)
#         return res
    
#     def dfs(self, digits, i, part, res):
#         # base case
#         if i >= len(digits):
#             res.append("".join(part))
#             return
#         # recursive exploration
#         for c in self.getLetters(digits[i]):
#             part.append(c) # add the current letter to the combination
#             self.dfs(digits, i + 1, part, res) # Recursive call for the next digit
#             part.pop() # backtrack
    
#     def getLetters(self, digit):
#         digit_to_letters = {
#             "2": "abc", "3": "def", "4": "ghi",
#             "5": "jkl", "6": "mno", "7": "pqrs",
#             "8": "tuv", "9": "wxyz"
#         }
#         return digit_to_letters.get(digit, "")
    # Time Complexity: O(3^n * 4^m), where n is the number of digits in the input that maps to 3 letters (e.g. 2, 3, 4, 5, 6, 8) and m is the number of digits in the input that maps to 4 letters (e.g. 7, 9), and n + m is the total number digits in the input.
    # Space Complexity: O(3^n * 4^m), since one has to keep 3^n * 4^m solutions.

#        Root
#     /   |     \
#    a    b      c
#   /|\  /|\    /|\
#  d e f d e f d e f

# 1. Use recursion to traverse this tree depth-first
# 2. At each level of the recursion, we add one more letter to our current combination (represented by the path from the root to the current node)
# 3. Once we reach a leaf node, which happens when the length of our current combination is equal to the length of the input digits, we add the current combination to our results list.
# 4. Use backtracking by removing the last added letter when we return to a previous level of the tree and try another letter branch. (This is where the decision changes).

# Now that have the approach, how do we code this?
# 1. Initial Setup: Iniitalize a variable, res, to store the results. res = []
# 2. Base case: if the digits string is empty, we should immediately return an emtpy list
# if not digits: return res
# 3. Preparing for recursion: set up a helper function for the recursive part of the solution, with the correct parameters.
# def dfs(digits, i, part, res):
# 4. Mapping Digits to Letters: We need a way to map each digit to the corresponding letters. We can use a dictionary to do this.
# 5. Recursive Exploration: 
# base case: add a combination to the results when i >= len(digits), where i is the current index in the digits string.
# 6. How would we iterate over the letters mapped to digits[i] and make a recursive call to dfs for each letter? 
# for c in self.getLetters(digits[i]):
# 7. Backtracking: After exploring one branch (letter), we backtrack by removing the last letter from part before the next iteration of the loop. This prepares part for the next letter in the current digit.
# Can we code the backtracking step that happens after the recursive call in the dfs function?
# part.pop()

# NeetCode solution
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = { "2": "abc",
                        "3": "def",
                        "4": "ghi",
                        "5": "jkl",
                        "6": "mno",
                        "7": "pqrs",
                        "8": "tuv",
                        "9": "wxyz" }
        
        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in digitToChar[digits[i]]:
                print("i:", i, "| Char: ", c, "| curStr: ", curStr)
                backtrack(i + 1, curStr + c)
        
        if digits:
            backtrack(0, "")
        return res
    
# Test function
digits = "23"
s = Solution()
result = s.letterCombinations(digits)
print(result)

# Output. Note how after each path is exhausted there is a return to previous level (i = 0); this for loop has recursive control flow. Recursion continues until the base case is reached when a combination's length matches the input length, illustrating how control flow can be directed deeper into the function call,

i: 0 | Char:  a | curStr:    -> backtrack(0, "")
i: 1 | Char:  d | curStr:  a -> backtrack(1, "a")
i: 1 | Char:  e | curStr:  a -> backtrack(1, "a")
i: 1 | Char:  f | curStr:  a -> backtrack(1, "a")
i: 0 | Char:  b | curStr:    -> backtrack(0, "")
i: 1 | Char:  d | curStr:  b -> backtrack(1, "b")
i: 1 | Char:  e | curStr:  b -> backtrack(1, "b")
i: 1 | Char:  f | curStr:  b -> backtrack(1, "b")
i: 0 | Char:  c | curStr:    -> backtrack(0, "")
i: 1 | Char:  d | curStr:  c -> backtrack(1, "c")
i: 1 | Char:  e | curStr:  c -> backtrack(1, "c")
i: 1 | Char:  f | curStr:  c -> backtrack(1, "c")
['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']