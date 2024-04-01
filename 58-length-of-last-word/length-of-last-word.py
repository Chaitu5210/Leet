class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string_length=len(s)-1
        if string_length==0:
            return 1
        temp=0
        while string_length>=0:
            if s[string_length]==" " and temp==0:
                string_length=string_length-1
            elif s[string_length]!=" ":
                temp=temp+1
                string_length=string_length-1
            else:
                return temp
        return temp
        