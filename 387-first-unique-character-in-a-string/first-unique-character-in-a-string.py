class Solution:
    def firstUniqChar(self, s: str) -> int:
        Dict={}
        temp=0
        for i in range(len(s)):
            if s[i] not in Dict:
                Dict[s[i]]=0
            Dict[s[i]]=Dict[s[i]]+1
        for char in Dict:
            if Dict[char]==1:
                return s.index(char)
        return -1