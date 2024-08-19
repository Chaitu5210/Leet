class Solution:
    def isPalindrome(self, s: str) -> bool:
        list1="".join(char for char in s if char.isalnum())
        list1=list1.lower()
        print(list1,list1[::-1])
        if list1==list1[::-1]:
            return True
        return False