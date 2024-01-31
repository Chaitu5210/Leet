class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        if n==1:
            return True
        while n>=2 :
            if n==1:
                return True
            if n<4:
                return False
            if n%4==0:
                print(n)
                n=n/4
            else:
                return False
        return True
        