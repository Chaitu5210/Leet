class Solution:
    def reverseWords(self, s: str) -> str:
        stringstack=[]
        word=[]
        for i in range(len(s)):
            if s[i]!=" ":
                word.append(s[i])
            if s[i]==" " or i==len(s)-1:
                stringstack.append("".join(word))
                word=[]
        stringstack = list(filter(None, stringstack))
        resultstring=""
        while stringstack:
            resultstring=resultstring+stringstack.pop()+" " 
        return resultstring[:len(resultstring)-1]           
        