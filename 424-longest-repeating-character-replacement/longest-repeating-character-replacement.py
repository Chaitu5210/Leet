class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        Dict={}
        l=0
        temp=0
        for r in range(len(s)):
            Dict[s[r]]=1+Dict.get(s[r],0)
            while (r-l+1)-max(Dict.values()) > k:
                Dict[s[l]]=Dict[s[l]]-1
                l=l+1
            temp=max(temp,r-l+1)
        return temp
