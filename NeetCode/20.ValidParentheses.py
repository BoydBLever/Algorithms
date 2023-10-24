class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in '({[':
                stack.append(c)
            elif c == ')':
                if not stack or stack.pop() != '(':
                    return False
            elif c == '}':
                if not stack or stack.pop() != '{':
                    return False
            elif c == ']':
                if not stack or stack.pop() != '[':
                    return False
        return not stack
    
# Test processing function
    def test(self, s: str) -> None:
        print("Input: " + s)
        print("Output: " + str(self.isValid(s)))
        print()
# Test case:
s = Solution()
s.test("()")
s.test("()[]{}")
s.test("(]")
s.test("([)]")