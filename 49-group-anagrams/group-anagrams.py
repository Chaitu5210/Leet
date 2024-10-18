class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Dict = defaultdict(list)
        for word in strs:
            temp=list(word)
            temp.sort()
            temp=tuple(temp)
            Dict[temp].append(word)
        result=[]
        for values in Dict.values():
            result.append(values)
        return result
        