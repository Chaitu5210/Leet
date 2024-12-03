# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    list_root1 = []
    list_root2 = []

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def dfs1(root1):
            if not root1:
                return

            if not root1.left and not root1.right:
                self.list_root1.append(root1.val)

            dfs1(root1.left)
            dfs1(root1.right)

        def dfs2(root2):
    
            if not root2:
                return

            if not root2.left and not root2.right:
                self.list_root2.append(root2.val)

            dfs2(root2.left)
            dfs2(root2.right)



        dfs1(root1)
        dfs2(root2)

        if self.list_root1 == self.list_root2:
            result = True
        else:
            result = False

        self.list_root1.clear()
        self.list_root2.clear()

        return result
