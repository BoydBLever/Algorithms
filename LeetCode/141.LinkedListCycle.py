# https://leetcode.com/problems/linked-list-cycle/
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 1. Initialize two pointers, slow and fast, both starting at the head.
        slow, fast = head, head
        
        # 2. Move slow one step at a time and fast two steps at a time.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # 3. If there's a cycle, the fast pointer will catch up to the slow pointer.
            if slow == fast:
                return True
        
        # 4. If fast reaches the end of the list, there's no cycle.
        return False
#Neetcode
    # def hasCycle(self, head: Optional[ListNode]) -> bool:
    #     slow, fast = head, head

    #     while fast and fast.next:
    #         slow = slow.next
    #         fast = fast.next.next
    #         if slow == fast:
    #             return True
        
    #     return False