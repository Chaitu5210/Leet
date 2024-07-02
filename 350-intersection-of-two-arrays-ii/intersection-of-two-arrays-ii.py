class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        Dict1={}
        Dict2={}
        for i in range(len(nums1)):
            Dict1[nums1[i]]=1+Dict1.get(nums1[i],0)
        for i in range(len(nums2)):
            Dict2[nums2[i]]=1+Dict2.get(nums2[i],0)
        result=[]
        for value in Dict1:
            if value in Dict2:
                temp=min(Dict1[value],Dict2[value])
                for j in range(temp):
                    result.append(value)
        return result