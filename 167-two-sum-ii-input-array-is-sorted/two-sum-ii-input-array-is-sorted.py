class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen={}
        for i,n in enumerate(numbers):
            temp=target-numbers[i]
            if temp in seen:
                return [seen[temp]+1,i+1]
            seen[n]=i