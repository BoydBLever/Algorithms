# https://leetcode.com/problems/generate-parentheses/
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 1. Define a recursive helper function to generate combinations.
        def backtrack(current, open_count, close_count, n, result):
            # 2. If the current combination is of length 2n, add it to the result.
            if len(current) == 2 * n:
                result.append(current)
                return
            
            # 3. If there are open brackets remaining, add an open bracket and recurse.
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count, n, result)
            
            # 4. If there are close brackets remaining and they don't exceed the open brackets, add a close bracket and recurse.
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1, n, result)
        
        # 5. Initialize an empty list for results.
        result = []
        
        # 6. Start the backtrack process.
        backtrack("", 0, 0, n, result)
        
        return result
    
    #Neetcode solution
    # def generateParenthesis(self, n: int) -> List[str]:
    #     #only add open parenthesis if open < n
    #     #only add a closing parenthesis if closes < open
    #     #valid IIF open == closes == n

    #     stack = []
    #     res = []

    #     def backtrack(openN, closedN)
    #         if openN == closedN == n:
    #             res.append("".join(stack))
    #             return
            
    #         if openN < n:
    #             stack.append("(")
    #             backtrack(openN + 1, closedN)
    #             stack.pop()

    #         if closedN < openN:
    #             stack.append(")")
    #             backtrack(openN, closedN + 1)
    #             stack.pop

    #     backtrack(0,0)
    #     return res
            