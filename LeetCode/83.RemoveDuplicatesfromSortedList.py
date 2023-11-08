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
            # Why create a dummy node? Because we need to return the head of the list, and the head could be the first duplicate node, so we can create a dummy node to point to the head of the list. The dummy is not part of the original list and is used to handle the edge case of removing duplicates at the head without special conditions.
            dummy = ListNode(0, head)
            cur = dummy
            # We need to check if the current node (cur.next) and the next node (cur.next.next) exist, because if they don't exist, we can't compare their values.
            # the while loop check if there is a node after the current one (cur.next), and a node after that one as well (cur.next.next)
            while cur.next and cur.next.next:
                # This means that the node immediately after cur is a duplicate.
                if cur.next.val == cur.next.next.val:
                # Remove the link to the immediate next node (cur.next). The pointer that was pointing to the duplicate node now points to the node after the duplicate.
                    cur.next = cur.next.next
                else:
                    cur = cur.next
            # Return the head of the list, which is the node after the dummy node.
            return dummy.next
    # Time complexity: O(N) where N is the length of the list
    # Space complexity: O(1)