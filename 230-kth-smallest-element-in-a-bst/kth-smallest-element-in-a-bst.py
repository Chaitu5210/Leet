# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        list1=[]
        if root is None:
            return 0
        def dfs(root):
            if root is None:
                return
            list1.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        list1.sort()
        return list1[k-1]
        
        