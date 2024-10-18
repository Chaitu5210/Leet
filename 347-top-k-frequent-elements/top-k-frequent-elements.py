class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Dict={}
        for element in nums:
            if element not in Dict:
                Dict[element]=0
            Dict[element]+=1
        Desc_Dict=dict(sorted(Dict.items(),key=lambda items:items[1], reverse=True))
        print(Dict)
        print(Desc_Dict)
        result=[]

        for index,values in Desc_Dict.items():
            print("k is ",k)
            if k>0:
                print("Inside with k",k)
                result.append(index)
            k=k-1
        return result
        