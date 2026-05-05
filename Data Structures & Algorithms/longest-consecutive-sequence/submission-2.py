#Note that order of appearance in the array doesn't matter

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        memo = Counter(nums)
        n = len(nums)

        start = []
        for key, val in memo.items():
            if (key-1) not in memo:
                start.append(key)

        res =0
        for k in start:
            count = 1
            while k+1 in memo:
                count+=1
                k+=1
            res = max(count, res)
        return res