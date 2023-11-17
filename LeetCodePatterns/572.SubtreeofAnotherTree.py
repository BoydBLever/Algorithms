# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            
            def isSameTree(s, t):
                if not s and not t:
                    return True
                elif not s or not t:
                    return False
                elif s.val != t.val:
                    return False
                else:
                    return isSameTree(s.left, t.left) and isSameTree(s.right, t.right)
            
            if not root:
                return False
            elif isSameTree(root, subRoot):
                return True
            else:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

# Optimized with serialization
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(node):
            if not node:
                return "None,"
            return "Node(" + str(node.val) + ")," + serialize(node.left) + serialize(node.right)

        rootStr = serialize(root)
        subRootStr = serialize(subRoot)

        return subRootStr in rootStr
