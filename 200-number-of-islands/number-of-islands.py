class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        no_of_islands=0
        visited=set()
        rows , cols = len(grid), len(grid[0])
        print(rows,cols)
        def bfs(r,c):
            q=collections.deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                row,col=q.popleft()
                temp=[[0,1],[1,0],[0,-1],[-1,0]]
                for rt,ct in temp:
                    temp_row=row+rt
                    temp_col=col+ct
                    if temp_row in range(rows) and temp_col in range(cols) and grid[temp_row][temp_col]=="1" and (temp_row,temp_col) not in visited:
                        q.append((temp_row,temp_col))
                        visited.add((temp_row,temp_col))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visited:
                    bfs(r,c)
                    no_of_islands=no_of_islands+1
        return no_of_islands
        