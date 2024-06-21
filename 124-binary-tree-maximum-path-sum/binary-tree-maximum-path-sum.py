# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=[root.val]
        def dfs(root):
            if root is None:
                return 0
            leftsub=dfs(root.left)
            rightsub=dfs(root.right)

            leftsub=max(leftsub,0)
            rightsub=max(rightsub,0)
            res[0]=max(res[0],root.val+leftsub+rightsub)
            return root.val+max(leftsub,rightsub)
        dfs(root)
        return res[0]