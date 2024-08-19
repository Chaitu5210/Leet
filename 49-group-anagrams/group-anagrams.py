class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Dict=defaultdict(list)
        for string in strs:
            list1=[0]*26
            for letter in string:
                temp=ord(letter)-ord('a')
                list1[temp]=list1[temp]+1
            Dict[tuple(list1)].append(string)
        return Dict.values()