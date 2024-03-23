class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        Dict = {i: [] for i in range(numCourses)}
        visited=set()
        for crs,pre in prerequisites:
            Dict[crs].append(pre)
        def dfs(crs):
            if crs in visited:
                return False
            if crs is None:
                return True
            visited.add(crs)
            for neighbors in Dict[crs]:
                if not dfs(neighbors): return False
            visited.remove(crs)
            Dict[crs]=[]
            return True

        for crs in Dict:
            if not dfs(crs): return False
        return True
