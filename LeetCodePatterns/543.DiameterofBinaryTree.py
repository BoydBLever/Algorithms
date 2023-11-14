# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

            def dfs(node):
                if not node:
                    return 0
                # What is the height of the binary tree rooted at the left child of the current node ('node')?
                left = dfs(node.left)
                right = dfs(node.right)
                
                self.ans = max(self.ans, left + right)
                return max(left, right) + 1
    
            self.ans = 0
            dfs(root)
            return self.ans