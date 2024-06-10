class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right=0,len(nums)-1
        while(left<right):
            print(nums[left],nums[right])
            if nums[left]>nums[right]:
                left=left+1
            else:
                right=right-1
        return nums[left]