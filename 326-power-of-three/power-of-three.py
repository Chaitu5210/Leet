class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0 or n==2:
            return False
        if n==1:
            return True
        while n>=1 :
            if n==1:
                return True
            if n==2:
                return False
            if n%3==0:
                print(n)
                n=n/3
            else:
                return False
        return True
        