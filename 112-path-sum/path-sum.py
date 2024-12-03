# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        sum = 0

        def dfs(root, sum):

            if not root:
                return False

            print(f'for current root {root.val} and sum {sum}')
            
            if not root.left and not root.right:
                if sum + root.val == targetSum:
                    return True

            if dfs(root.left, sum + root.val) or dfs(root.right, sum + root.val):
                return True
            
            return False

        final_result = dfs(root, sum)

        return final_result