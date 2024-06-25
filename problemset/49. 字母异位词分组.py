class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        import collections
        HashMap = collections.defaultdict(list)
        for str_ in strs:
            key = "".join(sorted(str_))
            HashMap[key].append(str_)
        return list(HashMap.values())