class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        result = []
        for s in strs:
            hashmap[tuple(sorted(s))].append(s)
        for i in hashmap.values():
            result.append(i)
        return result