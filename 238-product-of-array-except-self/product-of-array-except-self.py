class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[]
        right=[]
        temp=1
        for i in range(len(nums)):
            left.append(temp)
            temp=temp*nums[i]
        temp=1
        for i in range(len(nums)-1,-1,-1):
            right.append(temp)
            temp=temp*nums[i]
        right.reverse()
        result=[]
        for i in range(len(nums)):
            result.append(left[i]*right[i])
        return result

            
        