class Solution:
    def isBalanced(self, nums: str) -> bool:
        nums_list = list(nums)

        even_index = 0
        odd_index = 0
        for i in range(len(nums)):
            if i%2 == 0:
                even_index += int(nums[i])
            else:
                odd_index += int(nums[i])

        return True if odd_index == even_index else False

        