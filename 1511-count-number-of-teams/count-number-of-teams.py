class Solution:
    def numTeams(self, rating: List[int]) -> int:
        result=0
        def checklesserthan(leftlist,element,rightlist):
            if len(leftlist)==0 or len(rightlist)==0:
                return False
            leftcounter=0
            rightcounter=0
            for i in range(len(leftlist)):
                if element > leftlist[i]:
                    leftcounter=leftcounter+1
            for i in range(len(rightlist)):
                if element < rightlist[i]:
                    rightcounter=rightcounter+1
            return leftcounter*rightcounter

        for i in range(len(rating)):
            result=result+checklesserthan(rating[:i],rating[i],rating[i+1:])
            result=result+checklesserthan(rating[i+1:],rating[i],rating[:i])
        return result
        