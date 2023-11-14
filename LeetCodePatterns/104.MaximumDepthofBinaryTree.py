class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            return max(left_depth, right_depth) + 1
# Time complexity: O(N)
# Space complexity: O(H) H is the height of the tree

#      3
#    /   \
#   9     20
#        /  \
#       15   7
# Output: 3
# The point to understand here is that the depth is relative to the node being considered as the root of the subtree. For the call, maxDepth(root = 9), we are considering the subtree where 9 is the root. In this subtree, there are no levels below 9, hence its depth is 1.
# The tree's overall depth, on the other hand, is measured from its actual root, which in this case is node 3. When calculating the depth from the actual root of the tree, we count all ndoes along the longest path from the root node down to the farthest leaf. But when considering a subtree, we count from the root of that subtree.