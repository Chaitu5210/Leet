class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        
        teams_count = []
        for each_grid in grid:
            teams_count.append(sum(each_grid))
        
        max_count = max(teams_count)
        index = teams_count.index(max_count)
        return index

        