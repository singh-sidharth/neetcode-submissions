class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
       l = 0
       r = len(heights)-1
       area = (r-l)*min(heights[r], heights[l])

       while l<r:
        if heights[l] < heights[r]:
            l+=1
        
        else:
            r-=1

        width = r-l
        height = min(heights[l], heights[r])
        curArea = width*height

        area = max(area, curArea)
       return area