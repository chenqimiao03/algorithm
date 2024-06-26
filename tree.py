class BSTree:

    class TreeNode:

        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def __init__(self) -> None:
        self._root = None

    def insert(self, val):
        pass

    def remove(self):
        pass

    def search(self):
        pass


class Trie:

    class TrieNode:

        def __init__(self) -> None:
            self.path = 0
            self.end = 0
            self.nexts = [None for i in range(26)]
            
    
    def __init__(self) -> None:
        self._root = type(self).TrieNode()

    def insert(self, word: str):
        """将字符串 word 插入前缀树中
        """
        root = self._root
        root.path += 1
        for i in range(len(word)):
            j = ord(word[i]) - ord('a')
            if root.nexts[j] is None:
                root.nexts[j] = type(self).TrieNode()
            root = root.nexts[j]
            root.path += 1
        root.end += 1

    def search(self, word: str):
        """返回前缀树中字符串 word 的实例个数
        """
        root = self._root
        for i in range(len(word)):
            j = ord(word[i]) - ord('a')
            if root.nexts[j] is None:
                return 0
            root = root.nexts[j]
        return root.end
    
    def prefix(self, p):
        """返回前缀树中以 p 为前缀的字符串个数
        """
        root = self._root
        for i in range(len(p)):
            j = ord(p[i]) - ord('a')
            if root.nexts[j] is None:
                return 0
            root = root.nexts[j]
        return root.path
        
    
    def delete(self, word):
        """从前缀树中移除字符 word
        """
        if self.search(word) > 0:
            root = self._root
            root.path -= 1
            for i in range(len(word)):
                j = ord(p[i]) - ord('a')
                root.nexts[j].path -= 1
                if root.nexts[j].path == 0:
                    root.nexts[j] = None
                    return
                root = root.nexts[j]
            root.end -= 1