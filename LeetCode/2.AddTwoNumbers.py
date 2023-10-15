# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Initialize a dummy node and a current pointer starting at the dummy.
        dummy = ListNode()
        current = dummy
        
        # 2. Initialize carry to hold overflow.
        carry = 0
        
        # 3. Iterate through both linked lists.
        while l1 or l2:
            # Get the values from the nodes, if present.
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the total sum and the carry.
            total = val1 + val2 + carry
            carry = total // 10
            
            # Add the sum to the new linked list.
            current.next = ListNode(total % 10)
            current = current.next
            
            # Move to the next nodes, if present.
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        # 4. If there's any remaining carry, add it as a new node.
        if carry:
            current.next = ListNode(carry)
        
        # 5. Return the next node of the dummy (actual start of the resultant linked list).
        return dummy.next
#Neetcode
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            # 15
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # 8 + 7
        return dummy.next

