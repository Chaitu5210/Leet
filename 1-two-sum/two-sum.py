class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i in range(len(nums)):
            temp = target-nums[i]
            if temp in dict:
                return [dict[temp],i]
            dict[nums[i]]=i

        