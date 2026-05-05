class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        c = Counter(nums)
        if c.most_common()[0][1] > 1:
            return True
        return False