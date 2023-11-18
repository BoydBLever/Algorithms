# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # Base case
        if not root: return []
        # Initialize the paths list
        paths = []
        # define the dfs function with node and path as parameters
        def dfs(node, path):
            if not node: 
                return
            
            # Construct the path
            path += str(node.val)
            
            # Check if leaf node
            if not node.left and not node.right:
                paths.append(path)
                return
            
            # Recursive DFS calls to the left and right children
            # Include path + "->" to the recursive call because we need to add the arrow to the path
            dfs(node.left, path + "->")
            dfs(node.right, path + "->")
        
        # Initiate DFS with root and an empty string for the intitial path, and return results
        dfs(root, "")
        return paths