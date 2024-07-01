class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        temp=0
        for i in range(len(arr)):
            if arr[i]%2==1:
                temp=temp+1
                if temp==3:
                    return True
            else:
                temp=0
        return False
        