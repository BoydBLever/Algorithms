# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
            
            # 1. Find the middle node
            # Set two pointers: slow and fast
            slow = fast = head
            # The while loop finds the middle of the linked list
            while fast and fast.next:
                slow = slow.next # one step at a time
                fast = fast.next.next # two steps at a time
            # Slow pointers will be at the middle of the linked list when the while loop ends
            
            # 2. Reverse the second half
            # prev, slow and temp are pointers.
            # prev is the previous node of slow
            prev = None
            while slow:
                # save the next node to move to after the reversal of the current node
                temp = slow.next
                # reverse the current node's pointer to now point to what was previously its previous node
                slow.next = prev
                # prev is updated to slow, moving the prev pointer up to the current node, which has just been reversed
                prev = slow
                # slow is updated to temp, moving the slow pointer up to the next node in the list, which is the next node to be reversed.
                slow = temp
                # The while loop will continue until slow is None, which will be the end of the original list.
    
            # 3. compare the first and second half 
            while prev:
                # Compare the nodes from the beginning of the list (head) and the nodes from the reversed second half (prev).
                # If the values are not equal at any point, it means the list is not a palindrome.
                if prev.val != head.val:
                    return False
                # If the values are equal, both prev and head are moved forward to the next node in their sequences
                prev = prev.next
                head = head.next
    
            return True
    # Time complexity: O(N) where N is the length of the list
    # Space complexity: O(1)