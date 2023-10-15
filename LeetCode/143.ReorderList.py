# https://leetcode.com/problems/reorder-list/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        # Step 1: Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the list
        prev, curr = None, slow
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        
        # Step 3: Merge the two halves
        first, second = head, prev
        while second.next:
            first_next = first.next
            second_next = second.next
            
            first.next = second
            second.next = first_next
            
            first = first_next
            second = second_next
#Neetcode
    # def reorderList(self, head: Optional[ListNode]) -> None:
    #     slow, fast = head, head.next
    #     while fast and fast.next:
    #         slow = slow.next
    #         fast = fast.next.next
        
    #     # reverse second half
    #     second = slow.next
    #     prev = slow.next = None
    #     while second:
    #         tmp = second.next
    #         second.next = prev
    #         prev = second
    #         second = tmp
        
    #     # merge two halfs
    #     first, second = head, prev
    #     while second:
    #         tmp1, tmp2 = first.next, second.next
    #         first.next = second
    #         second.next = tmp1
    #         first = tmp1
    #         second = tmp2
    #         first, second = tmp1, tmp2


