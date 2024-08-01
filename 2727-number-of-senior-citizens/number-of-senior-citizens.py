class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count=0
        for i in range(len(details)):
            Temp_List=list(details[i])
            minitemp=int(Temp_List[11])
            print(int(Temp_List[11]))
            minitemp2=int(Temp_List[12])
            if minitemp>=6:
                if minitemp==6 and minitemp2==0:
                    pass
                else:
                    count=count+1
        return count
        