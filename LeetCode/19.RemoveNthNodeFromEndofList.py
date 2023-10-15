from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Initialize a dummy node and two pointers, first and second
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        
        # Move the first pointer n nodes ahead
        for _ in range(n + 1):
            first = first.next
        
        # Traverse the list with both pointers
        while first:
            first = first.next
            second = second.next
        
        # Remove the nth node from the end
        second.next = second.next.next
        
        # Return the new head
        return dummy.next
#Neetcode
    # def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    #     dummy = ListNode(0, head)
    #     left = dummy
    #     right = head

    #     while n > 0 and right:
    #         right = right.next
    #         n -= 1

    #     while right:
    #         left = left.next
    #         right = right.next

    #     # delete 
    #     left.next = left.next.next
    #     return dummy.next