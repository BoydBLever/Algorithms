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
            # The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node. 
            # Edge case: Check if the tree is empty. If it is, then return 0 because the depth of an empty tree is defined as 0.
            if not root:
                return 0
            # Initialize a queue. Append the root node to the queue. Initialize depth to 1. The purpose of using a queue is to store all the nodes of a particular level before moving on to the next level. The deque data structure is ideal for this purpose because it supports insertion and deletion from both the ends.
            queue = deque()
            queue.append(root)
            depth = 1
            # While the queue is not empty, perform the following steps:
            while queue:
                # Loop iterates over each node currently in the queue, which represents all the nodes at the current depth level. 
                for _ in range(len(queue)):
                    # Remove the first node from the queue (the next node in the current level) and assign it to node for processing.
                    node = queue.popleft()
                    # Check if the current node is a leaf node (a node with no children is a leaf node). If it's a leaf node, the function returns the current depth because we have reached the end of the tree.
                    if not node.left and not node.right:
                        return depth
                    # If the left child exists, append it to the queue.
                    if node.left:
                        queue.append(node.left)
                    # If the right child exists, append it to the queue.
                    if node.right:
                        queue.append(node.right)
                # After all nodes at the current depth level have been processed, increment the depth by 1. This prepares for processing the next level of nodes in the tree.
                depth += 1
    
            return depth