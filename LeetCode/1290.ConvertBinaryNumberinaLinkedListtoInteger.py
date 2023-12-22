# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # Initialize the result
        number = 0
        # Traverse the linked list
        while head is not None:
            # Shift left by one (equivalent to multiply by 2 in binary) and add the node's data
            number = (number << 1) | head.val
            head = head.next
            
        return number
# Time: O(N)
# Space: O(1)