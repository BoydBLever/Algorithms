class DynamicArray:

    # Constructor
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * capacity

    # Returns the ith element of the array
    def get(self, i: int) -> int:
        self.checkIndex(i)
        return self.array[i]

    # Sets the ith element of the array to n
    def set(self, i: int, n: int) -> None:
        self.checkIndex(i)
        self.array[i] = n
        
    # Adds an element to the end of the array
    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = n
        self.size += 1

    # Removes and returns the last element of the array
    def popback(self) -> int:
        if self.size == 0:
            raise IndexError('Index out of bounds')
        self.size -= 1
        return self.array[self.size]

    # Helper function to resize array
    def resize(self) -> None:
        self.capacity *= 2
        temp = [None] * self.capacity
        for i in range(self.size):
            temp[i] = self.array[i]
        self.array = temp

    # Helper function to get size  
    def getSize(self) -> int:
        return self.size

    # Helper function to get capacity
    def getCapacity(self) -> int:
        return self.capacity

    # Helper function to check if index is out of bounds
    def checkIndex(self, i: int) -> None:
        if i < 0 or i >= self.size:
            raise IndexError('Index out of bounds')