# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:

        sum = 0

        def dfs(root, sum):
            
            if not root:
                return sum

            if not root.left and not root.right:
                sum = sum + root.val

            sum = dfs(root.left, sum)
            sum = dfs(root.right, sum)

            return sum

        leaf_sum = dfs(root,sum)

        if leaf_sum == root.val:
            return True
        else:
            return  False        