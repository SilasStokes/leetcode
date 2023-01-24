

class TrieTree:
    class TrieNode:
        def __init__(self,end = False):
            self.children = {}
            self.end=end
     
    def __init__(self):
        self.root = self.TrieNode()