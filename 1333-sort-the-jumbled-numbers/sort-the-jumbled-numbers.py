class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def map_number(num: int) -> int:
            mapped_num_str = ''.join(str(mapping[int(digit)]) for digit in str(num))
            return int(mapped_num_str)
        
        mapped_pairs = [(num, map_number(num)) for num in nums]
        
        mapped_pairs.sort(key=lambda x: x[1])
        
        sorted_nums = [num for num, mapped_value in mapped_pairs]
        
        return sorted_nums
        