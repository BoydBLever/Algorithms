class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)  # Create a dummy node to hold the sorted list
        curr = head
        
        while curr:
            prev = dummy  # Start from the beginning of the sorted list for each new node
            
            # Find the correct position to insert the current node
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            
            # Insert the current node to the sorted list
            next_temp = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = next_temp
        
        return dummy.next
        