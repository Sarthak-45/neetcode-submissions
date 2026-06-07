class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left, right = 0, 0
        maxi = 0
        my_dict = {}
        for i in range(0,n):
            if s[right] in my_dict:
                left = max(left, my_dict[s[right]] + 1)
            maxi = max(maxi, right - left + 1)
            my_dict[s[right]] = right
            right += 1
        return maxi
