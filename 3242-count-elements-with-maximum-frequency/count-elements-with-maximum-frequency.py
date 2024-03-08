class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        Dict = {}
        subtemp=0
        for i in range(len(nums)):
            if nums[i] not in Dict:
                Dict[nums[i]]=0
            Dict[nums[i]]=Dict[nums[i]]+1
        temp=max(Dict)
        max_key = max(Dict, key=Dict.get)
        temp=Dict[max_key]
        for i in Dict:
            if Dict[i]==temp:
                subtemp=subtemp+temp
        return subtemp
        


