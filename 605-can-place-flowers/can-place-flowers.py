class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if i==len(flowerbed)-1 and flowerbed[i]==0 and flowerbed[i-1]==0:
                n=n-1
                flowerbed[i]=1
                continue
            if flowerbed[i]==0 and i==0 and flowerbed[i+1]==0:
                n=n-1
                flowerbed[i]=1
                continue
            if flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
                n=n-1
                flowerbed[i]=1
                continue
        return True if n<=0 else False

                
        