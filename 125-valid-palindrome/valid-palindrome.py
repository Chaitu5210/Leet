class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp="".join(char for char in s if char.isalnum())
        temp=temp.lower()
        print(temp)
        if temp==temp[::-1]:
            return True
        return False
        