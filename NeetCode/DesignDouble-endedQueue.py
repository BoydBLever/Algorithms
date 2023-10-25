class Deque:
    
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

def test_deque() -> None:
    # create a new deque
    deque = Deque()
    
    # test isEmpty method
    assert deque.isEmpty() == True
    
    # test append method
    deque.append(1)
    
    # test isEmpty method again
    assert deque.isEmpty() == False
    
    # test popleft method
    assert deque.popleft() == 1
    
    # test isEmpty method again
    assert deque.isEmpty() == True

# call the test_deque function
test_deque()
print(test_deque(["isEmpty", "append", 1, "isEmpty"]))