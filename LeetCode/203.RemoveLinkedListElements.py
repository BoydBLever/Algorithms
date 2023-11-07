# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
            if not head:
                return None
            # dummy node
            dummy = ListNode(0, head)
            # cur is a pointer
            cur = dummy
            # The while loop will continue until cur.next is None, which will be the end of the original list.
            while cur.next:
                # If the value of the next node is equal to the target value, the next node is removed by pointing cur.next to the node after the next node.
                if cur.next.val == val:
                    cur.next = cur.next.next
                # If the value of the next node is not equal to the target value, cur is moved forward to the next node in the list.
                else:
                    cur = cur.next
            # The dummy node is returned, instead of head, for a few reasons. Dummy's next is the new head. If the original head was equal to the target value, it would be removed. If the original head was not equal to the target value, it would remain as the head. Either way, dummy.next is the head of the new list.
            return dummy.next
    # Time complexity: O(N) where N is the length of the list
    # Space complexity: O(1)