class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        list1 = list(reversed(word1))
        list2 = list(reversed(word2))
        result=""
        minlength=min(len(word1),len(word2))
        for i in range(minlength):
            result=result+list1.pop()
            result=result+list2.pop()
        list1=reversed(list1)
        list2=reversed(list2)
        if list1:
            result=result+"".join(list1)
        if list2:
            result=result+"".join(list2)
        return result
            
        