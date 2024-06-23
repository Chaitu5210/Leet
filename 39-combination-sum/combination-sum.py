class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        temp=[]
        result=[]
        def dfs(temp):
            if sum(temp)>target:
                return False
            if sum(temp)==target:
                temp.sort()
                if temp not in result:
                    copying=temp.copy()
                    result.append(copying)
                    print(result)
            for i in candidates:
                temp.append(i)
                dfs(temp)
                temp.remove(i)
        dfs(temp)
        return result
            
        