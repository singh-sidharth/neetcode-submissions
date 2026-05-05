class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #find the bigges monotonic increasing sequence
        start= 0
        best = 0
        i = 1
        n= len(prices)
        for i in range(1,n):
            if prices[i]>=prices[start]:
                best = max(best, prices[i]-prices[start])
            else:
                start = i
        return best