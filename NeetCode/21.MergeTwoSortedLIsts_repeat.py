# https://leetcode.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# L1 1->2->4
# L2 1->3->4
# Output: take 1 from L1, and move to the next one. The only catch here is that output list is empty. We can create a dummy node, and it's a common technique and we avoid the edge case of the empty list. So we have a dummy node, then we insert 1 into the list. Compare values from list1 and list2, and insert the smaller node into the output. Then we continue to compare until we are at the last value of the lists. Then we append the rest of the list to the output.

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        #while they are not empty
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        #if one of the lists is empty, append the other one
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next