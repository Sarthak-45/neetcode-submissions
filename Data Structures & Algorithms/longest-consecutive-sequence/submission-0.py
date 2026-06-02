class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in myset:
                x = num
                count = 1
                while x + 1 in myset:
                    x += 1
                    count += 1
                longest = max(longest,count)
        return longest