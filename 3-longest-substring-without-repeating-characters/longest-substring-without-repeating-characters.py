class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        if len(s)==1:
            return 1
        
        first=0
        second=1
        lst=[]
        lst.append(s[first])
        length=0
        while second<len(s):
            if s[second] in lst:
                length=max(len(lst),length)
                index=lst.index(s[second])
                lst=lst[index+1::]
                lst.append(s[second])
                second=second+1
                first=first+1
            else:
                lst.append(s[second])
                second=second+1
                length=max(len(lst),length)
        return length

            
        
        