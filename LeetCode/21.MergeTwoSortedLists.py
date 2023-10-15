# https://leetcode.com/problems/merge-two-sorted-lists/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy node and set current to dummy
        dummy = ListNode()
        current = dummy
        
        # Traverse both lists until one of them is exhausted
        while list1 and list2:
            # If list1's value is smaller or equal, attach it to current and move list1's pointer
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            # If list2's value is smaller, attach it to current and move list2's pointer
            else:
                current.next = list2
                list2 = list2.next
            # Move the current pointer
            current = current.next
        
        # If list1 is not exhausted, attach the remaining nodes
        if list1:
            current.next = list1
        # If list2 is not exhausted, attach the remaining nodes
        else:
            current.next = list2
        
        # Return the merged list starting from the next of the dummy node
        return dummy.next

#Neetcode solution
    # def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #     dummy = ListNode()
    #     tail = dummy

    #     while l1 and l2:
    #         if l1.val < l2.val:
    #             tail.next = l1
    #             l1=l1.next
    #         else:
    #             tail.next = l2
    #             l2 = l2.next
    #         tail = tail.next

    #     if l1:
    #         tail.next = l1
    #     elif l2:
    #         tail.next = l2

    #     return dummy.next
