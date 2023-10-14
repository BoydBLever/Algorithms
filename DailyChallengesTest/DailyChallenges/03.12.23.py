# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        
        # recursively divide the list into two halves and merge them
        def merge(l, r):
            if not l or not r:
                return l or r
            
            if l.val < r.val:
                l.next = merge(l.next, r)
                return l
            else:
                r.next = merge(l, r.next)
                return r
        
        # merge the left and right halves of the list
        def mergeLists(lists, l, r):
            if l == r:
                return lists[l]
            elif l < r:
                mid = (l + r) // 2
                left = mergeLists(lists, l, mid)
                right = mergeLists(lists, mid+1, r)
                return merge(left, right)
            else:
                return None
        
        return mergeLists(lists, 0, len(lists)-1)
    
# To merge k sorted linked lists, we can use a divide-and-conquer approach similar to merge-sort. We can divide the k lists into two groups and recursively merge the two groups until we are left with a single merged list.

# In this implementation, the merge function takes two linked lists l and r and merges them into a single linked list. The mergeLists function recursively divides the lists into two halves and merges them using the merge function. Finally, mergeLists returns the merged linked list.

# The time complexity of this solution is O(n log k), where n is the total number of nodes across all linked lists and k is the number of linked lists. The space complexity is O(log k) due to the recursive stack.