# https://leetcode.com/problems/merge-two-sorted-lists/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Handle the edge cases
        if not list1:
            return list2
        if not list2:
            return list1
        
        # Create a dummy node to start the merged list
        head = ListNode()
        cur = head # Pointer to the dummy node. Continually append to cur without losing reference to the head of the merged list
        
        # Compare the values of the current nodes of list1 and list2. 
        while list1 and list2:
            # If list1's value is smaller, attach it to cur and move list1's pointer
            if list1.val <= list2.val:
                # attach list1's current node to the end of the merged list
                cur.next = list1
                # After attaching the smaller node to the merged list, you advance the pointer for the list from which you took the node
                list1 = list1.next
            # If list2's value is smaller, attach it to cur and move list2's pointer
            else:
                # Attach list2's current node to the end of the merged list
                cur.next = list2
                # After attaching the smaller node to the merged list, you advance the pointer for the list from which you took the node
                list2 = list2.next
            # Move the cur pointer forward to the node that was just attached to the merged list. This is done so that we can attach the next node to the end of the merged list.
            cur = cur.next
        # Termination conditions after the while loop: the loop continues until one of the lists is exhausted, meaning one of the pointers reaches the end of the list, becoming None. The lists may be of different lengths so we need to check and make sure every node is attached to the merged list.
        # If list1 is not exhausted, attach the remaining nodes
        if list1:
            cur.next = list1
        # If list2 is not exhausted, attach the remaining nodes
        else:
            cur.next = list2
        # Return the merged list
        return head.next

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
