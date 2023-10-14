# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        # 1. Initialize a stack to keep track of open brackets.
        stack = []
        
        # 2. Create a mapping for the brackets.
        mapping = {")": "(", "}": "{", "]": "["}
        
        # 3. For each character in the string:
        for char in s:
            # 4. If the character is a closing bracket:
            if char in mapping:
                # 5. Pop the topmost element from the stack.
                # If the stack is empty, assign a dummy value.
                top_element = stack.pop() if stack else '#'
                
                # 6. Check if the popped bracket matches the current character's mapping.
                # If not, return False.
                if mapping[char] != top_element:
                    return False
            else:
                # 7. If it's an open bracket, push it onto the stack.
                stack.append(char)
        
        # 8. After processing all characters, if the stack is empty, return True.
        # Otherwise, return False.
        return not stack
    
    #Neetcode solution
    # def isValid(self, s:str) -> bool:
    #     stack = []
    #     closeToOpen = {")" : "(", "]" : "[", "}" : "{"}

    #     for c in s:
    #         if c in closeToOpen:
    #             if stack and stack[-1] == closeToOpen[c]:
    #                 stack.pop()
    #             else:
    #                 return False
    #         else:
    #             stack.append(c)

    #     return True if not stack else False 