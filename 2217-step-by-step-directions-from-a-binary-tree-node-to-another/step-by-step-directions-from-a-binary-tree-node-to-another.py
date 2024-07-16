# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfs(node,string,target):
            if not node:
                return ""
            if node.val == target:
                return string
            string.append("L")
            res = dfs(node.left,string,target)
            if res:
                return string
            string.pop()
            string.append("R")
            res = dfs(node.right,string,target)
            if res:
                return string
            string.pop()
            
        i=0
        start=dfs(root,[],startValue)
        end=dfs(root,[],destValue)
        print(start,end)
        while i<min(len(start),len(end)):
            if start[i]!=end[i]:
                break
            i=i+1
        print(i)
        finalresult=(["U"] * len(start[i:]) + end[i:])
        return "".join(finalresult)