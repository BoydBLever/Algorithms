# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional, ListNode
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
       # head variable points to the dummy node to help reference the start of the new list. Head doesn't extend or change, it's always pointing to the dummy node. The dummy node is the first node in the new list.
        dummy = ListNode(0)
        # curr is a pointer that you move along as you merge the lists. The purpose of the curr pointer is to help reference the end of the new list.
        tail = dummy
        
        # if the value of the node at list1 is less than the value of the node at list2, then add the value at list1 to the new list by setting curr.next to list1. What is curr.next? curr.next is the next node in the new list. Then, move the list1 pointer to the next node in list1.
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            # if the value of the node at list2 is less than or equal to the value at list1, then add the value at list2 to the new list by setting curr.next to list2. Then, move list2 to the next node in list2.
            else:
                tail.next = list2
                list2 = list2.next
            # move curr to the next node in the new list. Curr is a pointer that you move along as you merge the lists. The purpose of the curr pointer is to help reference the end of the new list. Curr will point to the last node that was added to the merged list.
            tail = tail.next
            
            if list1:
                tail.next = list1
            if list2:
                tail.next = list2
            # Return head.next as the head of the merged linked list
            return tail.next
    # Time: O(n) Space: O(1)

    # NeetCode Solution
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next
    # Time: O(n) Space: O(1)