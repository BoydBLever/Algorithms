# https://leetcode.com/problems/copy-list-with-random-pointer/
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # 1. Iterate through the original list and create a copy of each node.
        # Use a dictionary to store the mapping between the original node and its copy.
        mapping = {}
        current = head
        while current:
            mapping[current] = Node(current.val)
            current = current.next
        
        # 2. Iterate through the original list again.
        current = head
        while current:
            # Set the next pointer of the copied node
            if current.next:
                mapping[current].next = mapping[current.next]
            # Set the random pointer of the copied node
            if current.random:
                mapping[current].random = mapping[current.random]
            current = current.next
        
        # 3. Return the copied version of the head.
        return mapping[head]
#Neetcode
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = { None: None }
        
        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        
        return oldToCopy[head]