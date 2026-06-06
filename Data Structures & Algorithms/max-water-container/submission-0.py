class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        area = 0
        i = 0
        j  = n - 1
        while i < j:
            width = j - i
            height = min(heights[i],heights[j])
            area = max(area, width * height)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return area