class Solution:
    def reverseVowels(self, s: str) -> str:
        left=0
        right=len(s)-1
        stringlist=list(s)
        vowels=["a","e","i","o","u","A","E","I","O","U"]
        while(left<right):
            while stringlist[left] not in vowels and left < right:
                left=left+1
            while stringlist[right] not in vowels and left < right:
                right=right-1
            stringlist[right],stringlist[left]=stringlist[left],stringlist[right]
            left=left+1
            right=right-1            
        return "".join(stringlist)