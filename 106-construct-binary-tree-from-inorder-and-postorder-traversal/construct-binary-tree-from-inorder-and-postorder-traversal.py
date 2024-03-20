# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        head=TreeNode(postorder.pop())
        mid=inorder.index(head.val)
        head.right=self.buildTree(inorder[mid+1:],postorder)
        head.left=self.buildTree(inorder[:mid],postorder)
        return head
