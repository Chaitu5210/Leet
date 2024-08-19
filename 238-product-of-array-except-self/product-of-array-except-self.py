class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp=1
        leftside=[]
        rightside=[]
        for i in range(len(nums)):
            leftside.append(temp)
            temp=temp*nums[i]
        temp=1
        i=len(nums)-1
        while i>=0:
            rightside.append(temp)
            temp=temp*nums[i]
            i=i-1
        rightside.reverse()
        result=[1]*len(nums)
        for i in range(len(nums)):
            result[i]=leftside[i]*rightside[i]
        return result

# Time Complexity - O(n)
# Space Complexity - O(n)

            


                    
