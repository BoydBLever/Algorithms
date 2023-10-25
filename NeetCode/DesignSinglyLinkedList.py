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
        if not self.head:
            return False
        if index == 0:
            self.head = self.head.next
            return True

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
    def process(self, commands_values: List) -> List[int]:
        results = []
        i = 0
        while i < len(commands_values):
            command = commands_values[i]
            # Handle commands that don't have values following them
            if command == "getValues":
                results.append(self.getValues())
                i += 1
                continue

            value = commands_values[i+1]

            if command == "get":
                results.append(self.get(value))

            elif command == "insertHead":
                self.insertHead(value)
                results.append(None)
            elif command == "insertTail":
                self.insertTail(value)
                results.append(None)
            elif command == "remove":
                results.append(self.remove(value))

            i += 2
        return results


# Test the LinkedList class
ll = LinkedList()
print(ll.process(["insertTail", 1, "insertHead", 2, "insertHead", 3, "insertTail", 4, "getValues"]

                 ))
