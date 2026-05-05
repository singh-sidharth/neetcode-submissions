class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.endOfWord = True

    def search(self, word: str) -> bool:
       # will have to search recursiverly for 
       # every '.'

       def dfs(j: int, root: TrieNode)-> bool:
        cur = root

        for i in range(j, len(word)):
            c = word[i]
            # utilize all keys as root for next prefix:
            if c == '.':
                for child in cur.children.values():
                    if dfs(i+1, child):
                        return True
                # only return false if none of the keys match
                return False
            else:
                if c not in cur.children:
                    return False
                cur = cur.children[c]
        return cur.endOfWord

       return dfs(0,self.root)
