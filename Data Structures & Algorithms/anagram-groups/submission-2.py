class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            freq_count = {}
            for ch in word:
                freq_count[ch] = freq_count.get(ch,0) + 1
            key = tuple(sorted(freq_count.items()))
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        return list(groups.values())