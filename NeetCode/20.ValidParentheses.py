# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         for c in s:
#             if c in '({[':
#                 stack.append(c)
#             elif c == ')':
#                 if not stack or stack.pop() != '(':
#                     return False
#             elif c == '}':
#                 if not stack or stack.pop() != '{':
#                     return False
#             elif c == ']':
#                 if not stack or stack.pop() != '[':
#                     return False
#         return not stack
    
# # Test processing function
#     def test(self, s: str) -> None:
#         print("Input: " + s)
#         print("Output: " + str(self.isValid(s)))
#         print()
# # Test cases
# s = Solution()
# s.test("()")
# s.test("()[]{}")
# s.test("(]")
# s.test("([)]")

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Mapping of closing brackets to their corresponding opening brackets
        HashMap = {')': '(', '}': '{', ']': '['}
        
        for c in s:
            # Check if the character is a closing bracket
            if c in HashMap:
                # If the stack is empty, use a dummy value '#'. 
                # This is to prevent errors when using stack.pop().
                top_element = stack.pop() if stack else '#'
                
                # If the top element isn't the corresponding opening bracket, return False
                if HashMap[c] != top_element:
                    return False
            else:
                # If it's an opening bracket or any other character, push onto the stack
                stack.append(c)
        
        # The stack should be empty if all brackets are matched
        return not stack
# Test processing function
    def test(self, s: str) -> None:
        print("Input: " + s)
        print("Output: " + str(self.isValid(s)))
        print()
# Test cases
s = Solution()
s.test("()")
s.test("()[]{}")
s.test("(]")