# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Handle edge case: if the list is empty, there is no cycle
        if head is None:
            return False
        # Use two pointers, one slow and one fast, to traverse the list. Slow starts at the head, fast starts at the head.next. If there is a cycle, the two pointers will eventually meet. If there is no cycle, the fast pointer will reach the end of the list.
        slow = head
        fast = head.next
        # While the slow and fast pointers are not pointing to the same node, traverse the list.
        while slow != fast:
            # If the fast pointer reaches the end of the list, there is no cycle.
            # if the list has an odd number of nodes and no cycle, then fast.next will become None when fast is at the penultimate node, because there is no node after the last one. If we only checked for fast == None, we would miss this and attempt to access fast.next.next on the next iteration, which would result in trying to access the next attribute of a NoneType, causing an error.
            if fast is None or fast.next is None:
                return False
            fast = fast.next.next
            slow = slow.next
        # If slow and fast are pointing to the same node, there is a cycle; return True. This means the rabbit caught up to the tortoise.
        # This solution uses Floyd's Cycle-Finding Algorithm and is an efficient way to find a cycle in a linked list.
        return True