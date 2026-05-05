class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        memo = Counter(nums)

        # an array to contain buckets
        array = [[] for i in range(len(nums) + 1)]

        # bucket sort
        for key,v in memo.items():
            array[v].append(key)

        res = []        
        for i in reversed(array):
           res.extend(i)
           if len(res) == k:
            return res       # Return res when t equals k
