class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict1 = dict()
        n = len(nums)
        for num in nums:
            dict1[num] = dict1.get(num,0) + 1
            if dict1[num] > 1:
                return True
            
        return False