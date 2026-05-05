# in the following two pointers
# l and r are the i for maxLeft array and maxRight array case
class Solution:
    def trap(self, height: List[int]) -> int:        
        l=0
        r = len(height)-1
        
        leftMax, rightMax = height[l], height[r]
        max_area = 0
        while l<r:
            if leftMax < rightMax:
                l+=1
                # space optimization part maxLeft
                leftMax = max(leftMax, height[l])
                max_area += leftMax-height[l]
            else:
                r-=1
                #space optimzation part for maxRight
                # even if h[r] was greater before now 
                # they're same so it will be 0 instead of negative
                rightMax = max(rightMax, height[r])
                max_area += rightMax - height[r]
        
        return max_area