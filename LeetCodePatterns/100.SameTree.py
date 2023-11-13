from typing import Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Depth-First Search Time: O(n) Space: O(n)
        # if both p and q are none, they are identical
        if p is None and q is None:
            return True
        # Handle the case where one of the trees is empty and the other is not.
        elif p is None or q is None:
            return False
        # Compare values of the current nodes in both trees. If the values are not equal, the trees are not identical.
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)