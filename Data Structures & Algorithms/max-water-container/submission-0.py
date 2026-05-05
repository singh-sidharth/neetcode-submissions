class Solution:
    def maxArea(self, heights: List[int]) -> int:
        size = len(heights)

        left = 0
        right = size-1
        maxArea = 0
        while left < right:
            curr = (right-left)*min(heights[left], heights[right])
            maxArea = max(maxArea, curr)
            if heights[left] < heights[right]:
                left+=1

            else:
                right-=1
        return maxArea