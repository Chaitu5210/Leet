class Solution:
    def customSortString(self, order: str, s: str) -> str:
        char_freq = {}
        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1
        result = ""
        for char in order:
            if char in char_freq:
                result += char * char_freq[char]
                del char_freq[char]
        for char, freq in char_freq.items():
            result += char * freq
        return result
