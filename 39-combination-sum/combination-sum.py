class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        temp=[]
        finallist=[]
        
        def dfs(temp):
            if sum(temp)==target:
                temp.sort()
                copylist=temp.copy()
                if copylist not in finallist:
                    finallist.append(copylist)
                temp=0
                return
            if sum(temp)>target:
                return False
            for num in candidates:
                temp.append(num)
                dfs(temp)
                temp.remove(num)
        dfs(temp)
        return finallist if len(finallist)!=0 else []   