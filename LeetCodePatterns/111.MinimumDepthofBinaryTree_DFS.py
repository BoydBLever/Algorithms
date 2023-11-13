class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node):
            # If it's a leaf node, return 1
            if not node.left and not node.right:
                return 1

            # Initialize the minimum depth to a large number
            min_depth = float('inf')

            # If the left child exists, explore it and calculate its depth
            if node.left:
                min_depth = min(min_depth, dfs(node.left))

            # If the right child exists, explore it and calculate its depth
            if node.right:
                min_depth = min(min_depth, dfs(node.right))

            # Return the minimum depth found plus one for the current node
            return min_depth + 1

        # Start DFS from the root node
        return dfs(root)
