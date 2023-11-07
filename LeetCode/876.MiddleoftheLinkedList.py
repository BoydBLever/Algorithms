# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
            # 1. find the length of the list
            length = 0
            cur = head
            while cur:
                length += 1
                cur = cur.next
            
            # 2. find the middle node
            middle = length // 2
            cur = head
            while middle:
                cur = cur.next
                middle -= 1
            
            return cur