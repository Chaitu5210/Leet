# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        def dfs(root,left,right):
            if root is None:
                return True
            if left >= root.val or root.val >= right:
                return False
            return (dfs(root.left,left,root.val) and dfs(root.right,root.val,right))
        return dfs(root,float("-inf"),float("inf"))
        