# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # if head is None:
        if head is None:
            return False
        # initialize two pointers
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            fast = fast.next.next
            slow = slow.next
        return True
    # Time: O(n)
    # Space: O(1)

# 1. Q: Why are there two pointers, fast and slow?
# A: The fast pointer moves two steps while the slow pointer moves one step at a time.
# If there is no cycle in the list, the fast pointer will eventually reach the end and we can return false in this case.
# If there is a cycle, the fast pointer will eventually meet with the slow pointer.

# 2. Q: Why initialize the fast point as head.next instead of head where the slow pointer is initialized?
# A: So that the fast pointer is ahead of the slow pointer by one step. Otherwise, they are both at the same node initially and the condition slow != fast will be false.

# 3. Q. Why check if fast is None or fast.next is None?
# A: If fast is None, there is no cycle in the list. If fast.next is None, there is no cycle in the list.

# 4. Q. What does it mean for the fast pointer to meet the slow pointer?
# A: It means that there is a cycle in the list. Otherwise, the fast pointer will reach the end first and the condition slow != fast will never be met.

#5. Q. Why can we be sure that the fast pointer will eventually meet the slow pointer if there is a cycle?
# A: Because the fast pointer is moving two steps at a time, while the slow pointer is moving just one step at a time, the fast pointer will eventually meet the slow pointer if there is a cycle. The fast pointer is iniatilized one step ahead of the slower pointer, so the only time they will be at the same node is if the fast pointer has caught up to it.

# 6. Q. What would happen if there were two slow pointers instead of a fast pointer and a slow pointer? 
# A: The two slow pointers would never meet since they are moving at the same speed. The fast pointer is necessary to catch up to the slow pointer.
# 7. Q. Can you think of a situation where this method would not work?
# A: If the list is empty, the fast pointer will be None and the condition fast.next is None will throw an error. We can fix this by checking if head is None at the beginning of the function and returning False if it is.
# 8. Q. Why is it safe to assume that if fast.next is None, there is no cycle in the list?
# A. Because fast.next equal to None means that the fast pointer is at the end of the list, and is not going is going to catch up to the slow pointer.

#9. Q. Can you explain why the loop continues while slow != fast?
# A. Fast moves 2 steps at a time. Slow moves 1 step at a time. Fast will equal slow when fast has caught up to slow. If there is a cycle, fast will eventually catch up to slow. If there is no cycle, fast will reach the end of the list and the loop will end.