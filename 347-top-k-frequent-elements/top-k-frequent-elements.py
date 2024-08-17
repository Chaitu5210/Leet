class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Dict={}
        result=[]
        for i in range(len(nums)):
            Dict[nums[i]]=1+Dict.get(nums[i],0)
        FinalList=dict(sorted(Dict.items(), key=lambda item:item[1],reverse=True ))
        resultlist=list(FinalList.keys())
        for i in range(k):
            result.append(resultlist[i])
        return result