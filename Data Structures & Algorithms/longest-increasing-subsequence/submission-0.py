# 1. A smaller subsequence cannnot start from within the subsequence
# as it would be the part of that subsequence
#
# 2. What is the longest subseqeunce I can form from a starting position?
# 3. Is it not the same as 1+length of longest subsequence from start
# 4. dp[i] = max(dp[i], (1+dp[i+1]) if (nums[i]< nums[i+1]) else 0)
#

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)