class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s = sum(piles)
        upper_bound = math.ceil((s/(h-len(piles)+1)))
        lower_bound = math.ceil((s/h))

        while lower_bound < upper_bound:
            mid = lower_bound + (upper_bound - lower_bound) // 2

            # calculate if mid can solve the solution
            current = 0
            for pile in piles:
                current += math.ceil(pile / mid)

            if current <= h:
                upper_bound = mid
            else:
                lower_bound = mid + 1
        return upper_bound
