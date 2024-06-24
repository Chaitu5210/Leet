class TriNode():
    def __init__(self):
        self.children={}
        self.endOfWord=False
    def addword(self,word):
        curr=self
        for letter in word:
            if letter not in curr.children:
                curr.children[letter]=TriNode()
            curr=curr.children[letter]
        curr.endOfWord=True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=TriNode()
        for word in words:
            root.addword(word)
        rows=len(board)
        cols=len(board[0])
        res=set()
        visited=set()
        def dfs(row,col,root,word):
            if row<0 or col<0 or row==rows or col==cols or board[row][col] not in root.children or (row,col) in visited:
                return
            visited.add((row,col))
            word=word+board[row][col]
            root=root.children[board[row][col]]
            if root.endOfWord:
                res.add(word)
            dfs(row+1,col,root,word)
            dfs(row-1,col,root,word)
            dfs(row,col+1,root,word)
            dfs(row,col-1,root,word)
            visited.remove((row,col))


        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root,"") 
        return res