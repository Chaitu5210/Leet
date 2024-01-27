class Solution:
    def reverseBits(self, n: int) -> int:
        stg=""
        bit=1
        for i in range(32):
            rst=n & bit
            if rst>=1:
                stg=stg+"1"
            else:
                stg=stg+"0"
            bit=bit<<1
        result=int(stg, 2)
        return result


        