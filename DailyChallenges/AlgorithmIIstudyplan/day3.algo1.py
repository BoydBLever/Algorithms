# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/?envType=study-plan&id=algorithm-ii
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Create a dummy node to keep track of the previous distinct node
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        
        while head:
            # Skip over all nodes with the same value
            while head.next and head.next.val == head.val:
                head = head.next
            
            # If the current node is a distinct node, link it to the previous distinct node
            if prev.next == head:
                prev = prev.next
            # If the current node is not a distinct node, skip over it
            else:
                prev.next = head.next
            
            head = head.next
        
        return dummy.next

# One approach to solve this problem is to use a dummy node to keep track of the previous distinct node, and iterate over the linked list to remove the duplicate nodes. We can compare the values of adjacent nodes to check if they are duplicates. If they are duplicates, we skip over all nodes with the duplicate value, and link the previous distinct node to the first node after the duplicates. If they are not duplicates, we update the previous distinct node to the current node
    
# This implementation has a time complexity of O(n), where n is the number of nodes in the linked list. Each node is visited once, and the operations performed on each node take constant time.