from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize previous, current, and next pointers
        prev = None
        curr = head
        
        # Traverse the list
        while curr is not None:
            next = curr.next  # Store next node
            curr.next = prev  # Reverse current node's pointer
            prev = curr  # Move to next node
            curr = next
            
        # Now, prev is pointing to the reversed list's head
        return prev
#Neetcode solution
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     #iterative solution
    #     prev, curr = None, head

    #     while curr:
    #         nxt = curr.next
    #         curr.next = prev
    #         prev = curr
    #         curr = nxt
    #     return prev
    
    #     #recursive solution
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if not head:
    #         return None
        
    #     newHead = head
    #     if head.next:
    #         newHead = self.reverseList(head.next)
    #         head.next.next = head
    #     head.next = None

    #     return newHead
    
    
