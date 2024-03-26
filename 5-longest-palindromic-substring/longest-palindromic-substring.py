class Solution:
    def longestPalindrome(self, s: str) -> str:
         string=""
         stringlen=0
         for i in range(len(s)):
             right,left=i,i
             #for odd
             while(left>=0 and right<=len(s)-1 and s[left]==s[right]):
                 if right-left+1>stringlen:
                     stringlen=right-left+1
                     string=s[left:right+1]
                 left=left-1
                 right=right+1
                 
             #for even
             left=i
             right=i+1
             while(left>=0 and right<=len(s)-1 and s[left]==s[right]):
                 if (right-left+1>stringlen):
                     stringlen=right-left+1
                     string=s[left:right+1]
                 left=left-1
                 right=right+1
         return string