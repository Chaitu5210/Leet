class Solution:
    def countBits(self, n: int) -> List[int]:
        tmp=1
        cnt=0
        lst=[]
        for i in range(n+1):
            for j in range(32):
                rst=i & tmp
                if rst>=1:
                    cnt=cnt+1
                tmp=tmp<<1
            lst.append(cnt)
            cnt=0
            tmp=1
        return lst
        