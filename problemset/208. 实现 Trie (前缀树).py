class Trie:

    class TrieNode:

        def __init__(self):
            self.nexts = {}
            self.end = 0

    def __init__(self):
        self._root = type(self).TrieNode()

    def insert(self, word: str) -> None:
        root = self._root
        for i in range(len(word)):
            if root.nexts.get(word[i]) is None:
                root.nexts[word[i]] = type(self).TrieNode()
            root = root.nexts[word[i]]
        root.end += 1

    def search(self, word: str) -> bool:
        root = self._root
        for i in range(len(word)):
            if root.nexts.get(word[i]) is None:
                return False
            root = root.nexts[word[i]]
        return not (root.end == 0)

    def startsWith(self, prefix: str) -> bool:
        root = self._root
        for i in range(len(prefix)):
            if root.nexts.get(prefix[i]) is None:
                return False
            root = root.nexts[prefix[i]]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)