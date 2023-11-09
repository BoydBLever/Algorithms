# https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Input: 1->2->3->4->5->NULL
# Reverse the links between nodes, and return the new head, which is the last node, 5.
# Output: 5->4->3->2->1->NULL
# This can be done two ways: iteratively, with two pointers, or recursively. We'll do it iteratively first. The two pointers are curr and prev. Curr is set to head (1) and prev is set to Null. For the first node 1, take the next pointer (which is a pointer, of course, but not considered one of the two pointers, curr and prev), and reverse the next pointer on 1, so it is pointing at Null. This is now going to be the last element in our new reversed linked list. So now we can shift our two pointers. Take our prev pointer and shift it to current, and take the current pointer, and shift it to the next node. Notice we broke the link between 1 and 2. We have to save this somewhere before we break it. So now our current is two, we want to take the next pointer (on two) and have it point at previous. And once again we are going to shift our prev pointer to current, and shift our current pointer to next. Finally, we are at the last node. Once again, we can update the next pointer of the current node. Shift the pointers again, and prev is going to be on 3, and current is going to be on null. Lucky for us, the previous pointer is going to be equal to the new head.
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        # T O(N) S O(1)
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
# Recursive solution: T O(N) S O(N)
# The best way to think about a recursive problem, is to break it down into recursive problems.
