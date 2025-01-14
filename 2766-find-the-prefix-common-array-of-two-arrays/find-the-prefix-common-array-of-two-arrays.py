class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        list_a = []
        list_b = []
        list_c = []

        for i in range(len(A)):
            list_a.append(A[i])
            list_b.append(B[i])
            list_c.append(len(list(set(list_a) & set(list_b))))

        return list_c



        