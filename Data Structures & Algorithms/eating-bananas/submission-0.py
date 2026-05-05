class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper_bound = max(piles)
        lower_bound = 1
        res = upper_bound

        while lower_bound <= upper_bound:
            mid = lower_bound + (upper_bound - lower_bound) // 2

            # calculate if mid can solve the solution
            current = 0
            for pile in piles:
                current += math.ceil(pile / mid)

            if current <= h:
                res = min(mid, res)
                upper_bound = mid - 1
            else:
                lower_bound = mid + 1
        return res
