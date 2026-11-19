class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        left = 0
        right = n-1

        max_total = 0
        while left < right:
            max_min = min(heights[left], heights[right])
            max_current = max_min * (right-left)

            max_total = max(max_total, max_current)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_total
