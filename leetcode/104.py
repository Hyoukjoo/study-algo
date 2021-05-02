# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        node = root
        depth = 0
        
        def dfs(b, d):
            nonlocal depth
            
            if b == None: return
            nd = d + 1
            if b.left is not None:
                dfs(b.left, nd)
            if b.right is not None:
                dfs(b.right, nd)
            depth = max(depth, nd)
        
        dfs(node, 0)
            
        return depth
