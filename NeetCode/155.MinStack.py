class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []  # This stack will keep track of minimums.

    def push(self, val: int) -> None:
        self.stack.append(val)
        # If the minStack is empty, or the new value is less than or equal to the current minimum,
        # push it onto the minStack.
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        # If the popped value is the current minimum, pop from the minStack as well.
        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Test processing function

def process_operations(input_list):
    operations = iter(input_list)
    obj = None
    result = []
    for op in operations:
        if op == "MinStack":
            obj = MinStack()
            result.append(None)
        elif op == "push":
            val = next(operations)
            obj.push(val)
            result.append(None)
        elif op == "pop":
            obj.pop()
            result.append(None)
        elif op == "top":
            result.append(obj.top())
        elif op == "getMin":
            result.append(obj.getMin())
    return result

input_sequence = ["MinStack","push", 5, "push", 3, "push", 7,"getMin","pop","top","getMin"]
print(process_operations(input_sequence))
