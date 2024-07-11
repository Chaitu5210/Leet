class Solution:
    def reverseParentheses(self, s: str) -> str:
        mainstring=list(s)
        stackholder=[]
        stackoutput=[]
        mainvariable=[]
        for i in range(len(s)):
            if s[i]==")":
                temp=stackholder.pop()
                while(temp!="("):
                    stackoutput.append(temp)
                    temp=stackholder.pop()
                mainvariable=stackholder
                stackoutput=stackoutput[::-1]
                while(stackoutput):
                    mainvariable.append(stackoutput.pop())
            else:
                stackholder.append(mainstring[i])
        return "".join(mainvariable) if len(mainvariable)>0 else s