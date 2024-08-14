class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1=list(s)
        list2=list(t)
        if len(list1)!=len(list2):
            return False
        for element in list1:
            if element in list2:
                list2.remove(element)
            else:
                return False
        return True
        