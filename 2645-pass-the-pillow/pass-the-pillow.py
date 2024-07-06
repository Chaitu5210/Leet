class Solution:
    # 1 2 3 4
    def passThePillow(self, n: int, time: int) -> int:
        pillow=1
        while(time>0):
            while pillow < n and time > 0:
                pillow = pillow + 1
                time = time - 1
            while pillow > 1 and time > 0:
                pillow = pillow - 1
                time = time - 1
        return pillow



            


        