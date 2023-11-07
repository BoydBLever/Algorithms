# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
            # It means just one thing if the head is empty: there is no list, no nodes, nothing to modify or delete.
            if not head:
                return None
            # Why create a dummy node? Because we need to return the head of the list, and the head could be the first duplicate node, so we need to create a dummy node to point to the head of the list.
            dummy = ListNode(0, head)
            cur = dummy
            while cur.next and cur.next.next:
                if cur.next.val == cur.next.next.val:
                    cur.next = cur.next.next
                else:
                    cur = cur.next
            
            return dummy.next
    # Time complexity: O(N) where N is the length of the list
    # Space complexity: O(1)