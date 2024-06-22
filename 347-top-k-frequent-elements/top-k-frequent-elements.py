class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Dict={}
        for i in nums:
            Dict[i]=1+Dict.get(i,0)
        seen=sorted(Dict,key=lambda x:-Dict[x])
        i=0
        list1=[]
        while k!=0:
            list1.append(seen[i])
            i=i+1
            k=k-1
        return list1
        