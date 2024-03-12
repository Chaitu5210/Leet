class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        temp=list(t)
        for i in range(len(s)):
            if s[i] in temp:
                temp.remove(s[i])
        return ' '.join(map(str, temp))