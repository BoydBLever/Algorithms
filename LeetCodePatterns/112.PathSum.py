# Credits to NeetCode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
            # Base case 
            if root is None:
                return False
            # Check if the root is a leaf node, if so, check if the targetSum is equal to the root value
            if root.left is None and root.right is None:
                return root.val == targetSum
            # Recursively call the function on the left and right subtrees
            return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
    # Time complexity: O(N) where N is the number of nodes in the tree
    # Space complexity: O(N) where N is the number of nodes in the tree
    # Example 1: Binary Tree
    #          5
    #        /   \
    #       4     8
    #      /     / \
    #     11    13  4
    #    /  \        \
    #   7    2        1
    # targetSum = 22
    # Output: True because 5->4->11->2 sums to 22
    # It's the recursive calls that identify the path. The base case is when the root is None, which means that the path doesn't exist.