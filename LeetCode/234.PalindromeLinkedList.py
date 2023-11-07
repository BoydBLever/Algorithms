# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
            
            # 1. find the middle node
            slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
    
            # 2. reverse the second half
            prev = None
            while slow:
                temp = slow.next
                slow.next = prev
                prev = slow
                slow = temp
    
            # 3. compare the first and second half nodes
            while prev:
                if prev.val != head.val:
                    return False
                prev = prev.next
                head = head.next
    
            return True
    # Time complexity: O(N) where N is the length of the list
    # Space complexity: O(1)