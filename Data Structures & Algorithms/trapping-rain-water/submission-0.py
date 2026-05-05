class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        total = 0

        leftMax, rightMax = height[left], height[right]
        while left<right:
            if leftMax<rightMax:
                left+=1
                leftMax = max(height[left], leftMax)
                total += leftMax - height[left]
            else:
                right-= 1
                rightMax = max(rightMax, height[right])
                total += rightMax - height[right]

        return total
            