# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    Dict = {}

    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        def dfs(root):
            if not root:
                return

            if root.val not in self.Dict:
                self.Dict[root.val] = 0
            self.Dict[root.val] += 1

            dfs(root.left)
            dfs(root.right)

        dfs(root)


        max_value = max(self.Dict.values())

        top_keys = [key for key, value in self.Dict.items() if value == max_value]

        self.Dict.clear()
        return top_keys