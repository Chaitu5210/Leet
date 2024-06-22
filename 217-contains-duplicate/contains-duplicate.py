class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        Dict={}
        for i in nums:
            if i in Dict:
                return True
            Dict[i]=0        


        return False