class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l=sqrt(num)
        if l==floor(l):
            return True
        else:
            return False
        