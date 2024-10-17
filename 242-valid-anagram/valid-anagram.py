class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temps=list(s)
        tempt=list(t)
        temps=sorted(s)
        tempt=sorted(t)
        if temps==tempt:
            return True
        return False
        