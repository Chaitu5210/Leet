# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        string=[]
        def dfs(root):
            if root is None:
                string.append("N")
                return
            string.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        print("final string is",string)
        dfs(root)
        return ",".join(string)

    def deserialize(self, data):
        vals=data.split(",")
        self.i=0
        print(vals)
        def dfs():
            if vals[self.i]=="N":
                self.i=self.i+1
                return None
            node=TreeNode(int(vals[self.i]))
            print(node.val)
            self.i=self.i+1
            print(self.i)
            node.left=dfs()
            node.right=dfs()
            return node
        return dfs()
