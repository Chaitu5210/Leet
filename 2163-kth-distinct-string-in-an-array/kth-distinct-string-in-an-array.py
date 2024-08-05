class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        Dict={}
        temp=1
        for i in range(len(arr)):
            if arr[i] not in Dict:
                Dict[arr[i]]=0
            Dict[arr[i]]=Dict[arr[i]]+1
        for key in Dict.keys():
            if Dict[key]==1:
                if temp==k:
                    return key
                temp=temp+1
        return ""
        