class MedianFinder:

    def __init__(self):
        self.lower=[]
        self.upper=[]
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lower,-1*num)
        if self.lower and self.upper and -1*self.lower[0]>self.upper[0]:
            val=-1*heappop(self.lower)
            heapq.heappush(self.upper,val)

        if len(self.lower)>len(self.upper)+1:
            val=-1*heapq.heappop(self.lower)
            heapq.heappush(self.upper,val)
        
        if len(self.upper) > len(self.lower)+1:
            val=-1*heapq.heappop(self.upper)
            heapq.heappush(self.lower,val)
            

    def findMedian(self) -> float:
        if len(self.lower) > len(self.upper):
            return -1*self.lower[0]
        if len(self.upper) > len(self.lower):
            return self.upper[0]
        return (-1*self.lower[0] + self.upper[0])/2        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()