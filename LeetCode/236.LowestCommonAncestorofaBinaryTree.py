# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            
            def dfs(root, p, q):
                if not root:
                    return None
                if root.val == p.val or root.val == q.val:
                    return root
                left = dfs(root.left, p, q)
                right = dfs(root.right, p, q)
                if left and right:
                    return root
                if not left:
                    return right
                if not right:
                    return left
    
            return dfs(root, p, q)
# Time complexity: O(N)
# Space complexity: O(N)
# root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Tree
#         3
#       /   \
#      5     1
#     / \   / \
#    6   2 0   8
#       / \
#      7   4
# The term "lowest" refers to the deepest level in the tree where the paths from the root to p and q meet.