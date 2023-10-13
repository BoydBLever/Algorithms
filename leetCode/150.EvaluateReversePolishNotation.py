# https://leetcode.com/problems/evaluate-reverse-polish-notation/
class Solution:
    def evalRPN(self, tokens):
        # 1. Initialize an empty stack.
        stack = []
        
        # 2. Define a set of operators.
        operators = set(["+", "-", "*", "/"])
        
        # 3. For each token in tokens:
        for token in tokens:
            # 4. If token is an operator:
            if token in operators:
                # 5. Pop two operands from the stack.
                operand2 = stack.pop()
                operand1 = stack.pop()
                
                # 6. Perform the operation and push the result back on the stack.
                if token == "+":
                    stack.append(operand1 + operand2)
                elif token == "-":
                    stack.append(operand1 - operand2)
                elif token == "*":
                    stack.append(operand1 * operand2)
                elif token == "/":
                    # Truncate towards zero
                    stack.append(int(operand1 / operand2))  
            else:
                # 7. If token is a number, push it onto the stack.
                stack.append(int(token))
        
        # 8. The result of the expression is on top of the stack.
        return stack[0]
    
#Neetcode
# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:
#         stack = []
#         for c in tokens:
#             if c == "+":
#                 stack.append(stack.pop() + stack.pop())
#             elif == "-":
#                 a, b = stack.pop(), stack.pop()
#                 stack.append(b - a)
#             elif == "*":
#                 stack.append(stack.pop() * stack.pop())
#             elif == "/":
#                 stack.append(int(b / a))
#             else:
#                 stack.append(int(c))
#         return stack[0]