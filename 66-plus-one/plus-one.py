class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        stg=""
        lst=[]
        for i in range(len(digits)):
            stg=stg+str(digits[i])
        tmp=int(stg)+1
        while tmp>0:
            tmp2=tmp%10
            lst.append(tmp2)
            tmp=tmp//10
        lst=lst[::-1]
        return lst
            

        