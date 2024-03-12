class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        j=0
        for i in range(len(nums1)):
            if nums1[i]==0 and j<len(nums2):
                nums1[i]=nums1[i]+nums2[j]
                j=j+1
        nums1.sort()

        """
        Do not return anything, modify nums1 in-place instead.
        """
        