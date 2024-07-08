class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends=[i for i in range(1,n+1)]
        length=len(friends)
        pointer=0
        while(len(friends)>1):
            pointer=pointer+k-1
            while(pointer >= len(friends)):
                pointer = pointer - len(friends)
            friends.remove(friends[pointer])
        return friends[0]