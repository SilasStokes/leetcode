# Runtime: 215 ms, faster than 73.27% of Python3 online submissions for Implement Trie (Prefix Tree).
# Memory Usage: 31.5 MB, less than 71.90% of Python3 online submissions for Implement Trie (Prefix Tree).

class Trie:
    class Node:
        def __init__(self):
            self.letters = {}
            self.isEnd = False

    def __init__(self):
        self.root = self.Node()
        

    def insert(self, word: str) -> None:
        temp = self.root
        last_index = len(word) - 1
        for i, c in enumerate(word):
            # add it to othe tree
            if c not in temp.letters:
                temp.letters[c] = self.Node()
            temp = temp.letters[c]
            
            if i == last_index:
                temp.isEnd = True
        
    def search(self, word: str) -> bool:
        temp = self.root
        last_index = len(word) - 1
        for i, c in enumerate(word):
            if c in temp.letters:
                if i == last_index and temp.letters[c].isEnd == True:
                    return True
                else:
                    temp = temp.letters[c]
            else:
                return False

    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        last_index = len(prefix) - 1
        for c in prefix:
            if c in temp.letters:
                temp = temp.letters[c]
            else: return False
        return True
        