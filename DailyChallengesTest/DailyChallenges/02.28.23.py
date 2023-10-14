# https://leetcode.com/problems/find-duplicate-subtrees/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def findDuplicateSubtrees(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[TreeNode]
    #     """
    def findDuplicateSubtrees(self, root):
        result, dict1 = [], defaultdict(int)
        
        def dfs(node):
            if not node:
                return "None"
            
            path = str(node.val)
            
            path += "." + dfs(node.left)
                
            path += "." + dfs(node.right)
            
            dict1[path] += 1
            
            if dict1[path] == 2:
                result.append(node)
                
            return path
        
        dfs(root)
        
        return result