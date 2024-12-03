# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        value = root.val

        def dfs(root):

            if not root:
                return False
            
            if root.val != value:
                return True

            return dfs(root.left) or dfs(root.right)



        return not(dfs(root))