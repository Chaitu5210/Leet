class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows=len(heights)
        cols=len(heights[0])
        pas,atl=set(),set()
        def dfs(row,col,visited,prev):
            if row < 0 or col < 0 or row==rows or col==cols or (row,col) in visited or heights[row][col] < prev:
                return
            visited.add((row,col))
            dfs(row+1,col,visited,heights[row][col])
            dfs(row-1,col,visited,heights[row][col])
            dfs(row,col+1,visited,heights[row][col])
            dfs(row,col-1,visited,heights[row][col])

        for c in range(cols):
            dfs(0,c,pas,heights[0][c])
            dfs(rows-1,c,atl,heights[rows-1][c])
        for r in range(rows):
            dfs(r,0,pas,heights[r][0])
            dfs(r,cols-1,atl,heights[r][cols-1])
        res=[]
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pas and (r,c) in atl:
                    res.append([r,c])
        return res