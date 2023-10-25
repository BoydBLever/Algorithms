from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None 

    def get(self, index: int) -> int:
        curr = self.head
        i = 0
        while curr and i < index:
            curr = curr.next
            i += 1
        return curr.val if curr else -1
        
    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
        
    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        
    def remove(self, index: int) -> bool:
        curr = self.head
        i = 0
        while curr and i < index - 1:
            curr = curr.next
            i += 1
        if not curr or not curr.next:
            return False
        curr.next = curr.next.next
        return True

    def getValues(self) -> List[int]:
        curr = self.head
        values = []
        while curr:
            values.append(curr.val)
            curr = curr.next
        return values
    
    # Test processing function 
    def process(self, commands: List[str], values: List[int]) -> List[int]:
        for i, command in enumerate(commands):
            if command == "get":
                values[i] = self.get(values[i])
            elif command == "insertHead":
                self.insertHead(values[i])
            elif command == "insertTail":
                self.insertTail(values[i])
            elif command == "remove":
                values[i] = self.remove(values[i])
        return values
    # Input ["insertHead", 1, "remove", 0]
    # Expected Output [None, True]
    print(process(["insertHead", 1, "remove", 0], [0, 0, 0, 0]))

