class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(s, open_count, close_count):
            # If the string s has reached 2 * n characters, add it to the results
            if len(s) == 2 * n:
                res.append(s)
                return
            
            # If the count of open parentheses is less than n, add an open parenthesis
            if open_count < n:
                backtrack(s + "(", open_count + 1, close_count)
            
            # If the count of close parentheses is less than the count of open parentheses, add a close parenthesis
            if close_count < open_count:
                backtrack(s + ")", open_count, close_count + 1)

        res = []
        backtrack("", 0, 0)
        return res
# Decision Tree for n = 2
#                  ""
#                 /  
#               "("    
#              /   \
#           "(("   "()" 
#           /       | 
#         "(()"   "()(" 
#          |       |
#       "(())"   "()()" 