class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        half=int(len(nums)/2)
        seen=set()
        for i in range(half):
            minimum=min(nums)
            maximum=max(nums)
            avarage=(minimum+maximum)/2
            nums.remove(minimum)
            nums.remove(maximum)
            seen.add(avarage)
        return len(seen)

            
        