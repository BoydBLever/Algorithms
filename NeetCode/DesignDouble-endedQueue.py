from typing import List
from collections import deque

class MyDeque:
    
    def __init__(self):
        # initialize an empty deque
        self.items = []
        
    def isEmpty(self) -> bool:
        # return True if the deque is empty
        return self.items == [] 

    def append(self, value: int) -> None:
        # add a value to the right end of the deque
        self.items.append(value)

    def appendleft(self, value: int) -> None:
        # add a value to the left end of the deque
        self.items.insert(0, value)

    def pop(self) -> int:
        # remove and return the value at the right end of the deque
        if self.isEmpty():
            return -1
        else:
            return self.items.pop()

    def popleft(self) -> int:
        # remove and return the value at the left end of the deque
        if self.isEmpty():
            return -1
        else:
            return self.items.pop(0)
        
# Time Complexity: O(1) for all operations
# Space Complexity: O(n) for n operations

def test_deque(operations: list) -> list:
    # create a new deque
    my_deque = MyDeque()
    
    results = []  # List to store results of operations
    i = 0  # Index to traverse operations list
    
    while i < len(operations):
        op = operations[i]
        
        if op == "isEmpty":
            results.append(my_deque.isEmpty())
        elif op == "append":
            # Next item in the list is the value to append
            value = operations[i + 1]
            my_deque.append(value)
            results.append(None)
            i += 1  # Increment index to skip the value we just processed
        elif op == "appendleft" or op == "appendLeft":
            # Next item in the list is the value to appendleft
            value = operations[i + 1]
            my_deque.appendleft(value)
            results.append(None)
            i += 1  # Increment index to skip the value we just processed
        elif op == "pop":
            results.append(my_deque.pop())
        elif op == "popleft":
            results.append(my_deque.popleft())
        elif op.lower() == "popleft":
            results.append(my_deque.popleft())

        
        i += 1  # Increment to process the next operation

    return results

# Test the function with your input
print(test_deque(["appendLeft", 1, "popLeft", "appendLeft", 2, "popLeft"]
)) 

my_deque = MyDeque()
print(my_deque.isEmpty()) # Expected: True
my_deque.appendleft(1)
print(my_deque.isEmpty()) # Expected: False