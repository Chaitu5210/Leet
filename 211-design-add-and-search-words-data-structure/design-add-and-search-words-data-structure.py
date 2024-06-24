class TrieNode():
    def __init__(self):
        self.children={}
        self.endOfWord=False

class WordDictionary:
    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        curr=self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter]=TrieNode()
            curr=curr.children[letter]
        curr.endOfWord=True

    def search(self, word: str) -> bool:
        def dfs(j,root):
            curr=root
            for i in range(j,len(word)):
                if word[i]==".":
                    for child in curr.children.values():
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    if word[i] in curr.children:
                        curr=curr.children[word[i]]
                    else:
                        return False
            return curr.endOfWord
        return dfs(0,self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)