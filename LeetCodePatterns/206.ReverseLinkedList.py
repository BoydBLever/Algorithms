# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            # Edge case: check if the list is empty.
            if not head:
                return None
            # prev is initalized to None because at the beginning of the reversal process, the new reversed list is empty, and the first node in the original list (which head points to) will end up being the last node in the reversed list, so its 'next' should be None. Prev represents the node that will be the new head of the reversed list.
            prev = None
            # cur is the current node we're looking to reverse the pointer for.
            cur = head
            while cur:
            # next temporarily stores the original next node of cur before the reversal of the pointer. This is because cur.next = prev reverses the pointer of the current node to point to what was previously the last node of the reversed list (initially None). Without storing cur.next in next, we would lost the reference to the rest of the original list as soon as you perform the reversal.
                next = cur.next
                cur.next = prev
                #prev is updated to be the current node (cur) which has just had its .next reference reversed.
                prev = cur
                # cur is then updated to the next node in the original list (next) which is the one that cur was pointing to before its .next was reversed
                cur = next
            # prev is the head of the reversed list.
            return prev
    
    # Time complexity: O(n) where n is the number of nodes in the list.
    # Space complexity: O(1) since we're not using any additional space.

    # Reversal process: we are modifying the next pointers of each node in the original list so that they point to the previous node instead, effectively reversing the direction of the list. This is done 1 node at a time, and at each step, only one pointer is changed. 

    # The reversal process is illustrated below:
    # Original list: 1 -> 2 -> 3 -> 4 -> 5 -> None
    # Reversed list: None <- 1 <- 2 <- 3 <- 4 <- 5
    