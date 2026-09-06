class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        MaxSum = nums[0]
        CurSum = 0
        for i in nums:
            if CurSum < 0:
                CurSum = 0
            CurSum += i
            MaxSum = max(CurSum, MaxSum)
        return MaxSum