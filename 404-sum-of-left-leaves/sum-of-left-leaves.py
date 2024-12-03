# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        sum = 0

        def dfs(root, sum, left):

            if not root:
                return sum

            print(root.val, sum)

            if not root.left and not root.right and left:
                sum = sum + root.val
                print(f' Root Value is {root.val} and Sum is {sum}')
                return sum

            sum = dfs(root.left, sum, left= True)
            sum = dfs(root.right, sum, left= False)

            return sum
            

        left = False
        return dfs(root, sum, left)