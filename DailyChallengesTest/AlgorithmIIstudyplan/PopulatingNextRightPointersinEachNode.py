"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        
        queue = [root]
        
        while queue:
            size = len(queue)
            prev = None
            
            for i in range(size):
                curr = queue.pop(0)
                
                if prev:
                    prev.next = curr
                
                if curr.left:
                    queue.append(curr.left)
                
                if curr.right:
                    queue.append(curr.right)
                
                prev = curr
            
            prev.next = None
        
        return root