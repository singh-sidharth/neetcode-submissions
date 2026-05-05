# Used to efficiently store strings
# Autocomplete and SpellChecker

class TrieNode:
    def __init__(self):
        self.children = {}
        self.wordEnd = False

class PrefixTree:

    def __init__(self):
        self.__root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.__root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.wordEnd = True

    def search(self, word: str) -> bool:
        cur = self.__root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        
        return cur.wordEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self.__root

        for c in prefix:
            if c not in cur.children:
                return False
            
            cur = cur.children[c]
        
        return True