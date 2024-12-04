class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:

        sentence_list = sentence.split()

        def checkword(target, word):
            if len(word) < len(target):
                return False
            temp = True
            for i in range(len(target)):
                if target[i] != word[i]:
                    return False
            return True


        for i in range(len(sentence_list)):
            if searchWord[0] == sentence_list[i][0]:
                if checkword(searchWord, sentence_list[i]):
                    return i+1
        return -1
        