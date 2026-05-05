class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        tempSum = 0

        # Two pointer while
        while left<right:
            tempSum = numbers[left] + numbers[right]
            if tempSum == target:
                return [left+1, right+1]
            if tempSum <= target:
                left+=1
            else:
                right-=1