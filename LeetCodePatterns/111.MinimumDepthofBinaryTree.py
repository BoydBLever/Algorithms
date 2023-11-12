# Definition for a binary tree node.
from typing import Optional, deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
            # BFS solution visits nodes level by level, starting from the root. Time: O(N), Space: O(N) 
            # Edge case: Check if the tree is empty. If it is, then return 0 because the depth of an empty tree is defined as 0.
            if not root:
                return 0
            # Initialize a queue. Append the root node to the queue. Initialize depth to 1. The purpose of using a queue is to store all the nodes of a particular level before moving on to the next level. The deque data structure is ideal for this purpose because it supports insertion and deletion from both the ends.
            queue = deque()
            queue.append(root)
            depth = 1
    
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    if not node.left and not node.right:
                        return depth
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                depth += 1
    
            return depth