from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize three pointers
        # previous, current, and next
        prev = None
        curr = head
        
        # Iterate through the list, with cur as the iterator
        while curr is not None:
            # Temporarily store the next node
            next = curr.next
            # Set curr.next to prev to reverse the pointer
            curr.next = prev
            # Advance the pointers one step forward
            prev = curr
            curr = next
            
        # Prev will be at the new head of the reversed list
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
    
    
