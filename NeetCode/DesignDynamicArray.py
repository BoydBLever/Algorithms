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
        
# Testcase processing function

def processTestcase(commands):
    # Create an instance of the DynamicArray class
    dynamic_array = DynamicArray(commands[1])
    output = [None]  # For the constructor call

    # Start iterating from the 2nd command onwards
    i = 2
    while i < len(commands):
        cmd = commands[i]
        if cmd == "pushback":
            dynamic_array.pushback(commands[i + 1])
            output.append(None)
            i += 2
        elif cmd == "get":
            output.append(dynamic_array.get(commands[i + 1]))
            i += 2
        elif cmd == "set":
            dynamic_array.set(commands[i + 1], commands[i + 2])
            output.append(None)
            i += 3
        elif cmd == "getCapacity":
            output.append(dynamic_array.getCapacity())
            i += 1
        elif cmd == "getSize":
            output.append(dynamic_array.getSize())
            i += 1
        elif cmd == "popback":
            output.append(dynamic_array.popback())
            i += 1
    return output

test_case = ["Array", 1, "getSize", "getCapacity", "pushback", 1, "pushback", 2, "pushback", 3, "pushback", 4, "pushback", 5, "pushback", 6, "pushback", 7, "pushback", 8, "pushback", 9, "getSize", "getCapacity", "popback", "popback", "popback", "popback", "popback", "popback", "popback", "popback", "popback", "getSize", "getCapacity"]
print(processTestcase(test_case))
