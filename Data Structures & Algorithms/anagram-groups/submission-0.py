class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s))
            hash[sorted_s].append(s)

        return list(hash.values())