# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional, ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev = None #prev pointer is set to null
        curr = head # curr pointer is set to head
        # prev, curr = None, head
        next = head.next
        while curr:
            curr.next = prev
            prev = curr
            curr = next
            if next:
                next = next.next
        return prev
    # Time: O(n) Space: O(1)

    # Recursive Solution
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
    # Time: O(n) Space: O(n)

    # NeetCode Solutions
    # iterative T O(n) M O(1)
    prev, curr = None, head 

    while curr:
        nxt = curr.next
        curr.next = prev 
        prev = curr 
        curr = nxt 
    return prev 
    
    
    # recursive T O(n) M O(n)
    if not head:
        return None
    
    newHead = head 
    if head.next:
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
    return newHead