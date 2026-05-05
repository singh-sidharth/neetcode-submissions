class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # initializinh
        res = max(nums)    
        curr_max = 1
        curr_min = 1

        for num in nums:
            # reset on zero
            if num == 0:
                curr_max, curr_min = 1, 1
                continue

            # calculations
            tmp = curr_max * num
            curr_max = max(num * curr_max, num*curr_min, num)
            # the max will reset but we need older value
            curr_min = min(tmp, num*curr_min, num)
            res = max(res, curr_max, curr_min)
        
        return res