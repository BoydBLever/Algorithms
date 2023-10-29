# NeetCode solution
# Definition for a binary tree node.
# NeetCode solution
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(root):
            if not root:
                return 
            # inorder traversal
            # go through left sub-tree
            inorder(root.left)
            # process the root node
            res.append(root.val)
            # do same recursive algo on right subtree
            inorder(root.right)
        inorder(root)
        return res

    # Iterative solution.
    # res = []
    # stack = []
    # cur = root

    # while cur or stack:
    #     whie cur:
    #         stack.append(cur)
    #         cur = cur.left
    #     cur = stack.pop()
    #     res.append(cur.val)
    #     cur = cur.right

    # return res