# https://leetcode.com/problems/min-stack/
class MinStack:

    # 1. Initialize two stacks: one for values and one for minimums.
    def __init__(self):
        self.stack = []
        self.min_stack = []

    # 1. Push the value onto the main stack.
    # 2. If the min_stack is empty or the current value is less than or equal to the top of min_stack, push it onto min_stack.
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    # 1. Pop the value from the main stack.
    # 2. If the popped value is equal to the top of min_stack, pop it from min_stack as well.
    def pop(self) -> None:
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    # 1. Return the top of the main stack.
    def top(self) -> int:
        return self.stack[-1]

    # 1. Return the top of the min_stack.
    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

#Neetcode solution
# class MinStack:

#     def __init__(self):
#         self.stack = []
#         self.minStack = []

#     def push(self, val:int) -> None:
#         self.stack.append(val)
#         val = min(val, self.minStack[-1] if self.minStack val)
#         self.minStack.append(val)

#     def pop(self) -> None:
#         self.stack.pop()
#         self.minStack.pop()

#     def top(self) -> int:
#         return self.stack[-1]
    
#     def getMin(self) -> int:
#         return self.minStack[-1]