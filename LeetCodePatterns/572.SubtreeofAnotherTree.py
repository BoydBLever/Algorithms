# 
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
# Remember the purpose of this algorithm is to check if subRoot is a subtree of root. Time complexity is O(m*n), where m is the number of nodes in root and n is the number of nodes in subRoot. Space complexity is O(m+n).    
# DFS Solution
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # First, check if subRoot is None. A 'None' tree is a subtree of any tree, so it returns True in this case.
        if not subRoot:
            return True
        # if root is None, then subRoot can't be a subtree of root, so it returns False.
        if not root:
            return False
        # Then it check if the tree rooted at root is the same as subRoot using the isSameTree helper function. If they are the same, it returns True.
        if self.isSameTree(root, subRoot):
            return True
        # If not, it recursively checks whether subRoot is a subtree of either the left or right subtree of root.
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    # This function checks whether two trees s and t are identical. It's a recursive function that performs a straightforward comparision of values.
    def isSameTree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        # If both s and t are None, then they are identical, so it returns True.
        if not s and not t:
            return True
        # If one of them is None, then they are not identical, so it returns False.
        if not s or not t:
            return False
        # If both of them are not None, then it checks if their values are the same. If not, they are not identical, so it returns False.
        if s.val != t.val:
            return False
        # If their values are the same, it recursively checks whether their left and right subtrees are identical.
        return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
    
    # Binary Tree
    # [3,4,5,1,2,null,null,null,null,0]
    #            3
    #           / \
    #          4   5
    #         / \
    #        1   2
    #       /           
    #      0    
