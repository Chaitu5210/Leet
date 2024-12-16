class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        for i in range(k):
            index = nums.index(min(nums))
            nums[index] = nums[index]*multiplier

        return nums     