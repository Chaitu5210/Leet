# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        count = 0

        def dfs(root, count):

            if not root:
                return count

            count = count + 1

            count = dfs(root.left, count)
            count = dfs(root.right, count)
            return count

        count = dfs(root,count)

        return count        