# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
            if not head:
                return None
            dummy = ListNode(0, head)
            cur = dummy
            while cur.next:
                if cur.next.val == val:
                    cur.next = cur.next.next
                else:
                    cur = cur.next
            
            return dummy.next
    # Time complexity: O(N) where N is the length of the list
    # Space complexity: O(1)