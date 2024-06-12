class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": return ""
        window,seent={},{}
        for elem in t:
            seent[elem]=1+seent.get(elem,0)
        left=0
        res,reslen=[-1,-1],float("infinity")
        first,second=0,len(seent)
        for right in range(len(s)):
            a=s[right]
            window[a]=1+window.get(a,0)
            if a in seent and window[a]==seent[a]:
                first=first+1
            while first==second:
                if right-left+1 < reslen:
                    res=[left,right]
                    reslen=right-left+1
                window[s[left]]-=1
                if s[left] in seent and window[s[left]]< seent[s[left]]:
                    first-=1
                left=left+1
        return "" if reslen == float("infinity") else s[res[0]:res[1] + 1]