class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_count = {}
        if len(s) != len(t):
            return False
        for ch in s:
            freq_count[ch] = freq_count.get(ch,0) + 1

        for ch in t:
            if ch not in freq_count:
                return False
            else:
                if freq_count[ch] == 0:
                    return False
                freq_count[ch] -= 1
        return True