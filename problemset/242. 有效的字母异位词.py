class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        HASHMAP = {}
        for c in s:
            if c not in HASHMAP:
                HASHMAP[c] = 1
            else:
                HASHMAP[c] += 1
        for c in t:
            if c not in HASHMAP:
                return False
            else:
                HASHMAP[c] -= 1
                if HASHMAP[c] == 0:
                    HASHMAP.pop(c)
        return not len(HASHMAP)