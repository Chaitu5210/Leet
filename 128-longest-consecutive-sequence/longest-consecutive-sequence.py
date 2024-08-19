class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1=set(nums)
        list1=list(set1)
        list1.sort()
        temp,result=0,0
        Dict={}
        for i in range(len(list1)):
            Dict[list1[i]]=Dict.get(list1[i],i)
        for i in range(len(list1)):
            if list1[i]+1 in Dict:
                temp=temp+1
            else:
                temp=0
            result=max(result,temp)
        return result+1 if len(nums)>0 else 0