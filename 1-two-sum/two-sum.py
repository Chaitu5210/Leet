class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Dict={}
        for i in range(len(nums)):
            temp=target-nums[i]
            if temp in Dict:
                return [Dict[temp],i]
            Dict[nums[i]]=i
        print(Dict)
        