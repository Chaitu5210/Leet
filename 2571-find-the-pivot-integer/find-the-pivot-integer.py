class Solution:
    def pivotInteger(self, n: int) -> int:
        numbers=[]
        for i in range(1,n+1):
            numbers.append(i)
        for pivot in range(n):
            first=sum(numbers[:pivot+1])
            second=sum(numbers[pivot:])
            if first==second:
                return pivot+1
        return -1
        