class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        for i in range(k):
            max_element = max(gifts)
            
            index = gifts.index(max_element)

            gifts[index] = int(sqrt(gifts[index]))

        
        return sum(gifts)
        