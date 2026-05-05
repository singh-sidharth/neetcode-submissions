class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        dq = deque()

        for j in range(k):
            while dq and nums[j] >= nums[dq[-1]]:
                dq.pop()
            dq.append(j)

        res.append(nums[dq[0]])

        for i in range(k, len(nums)):
            # remove begining of previous element if it was maximum
            if dq and dq[0] == i-k:
                dq.popleft()
            # remove all minimum from deque than the new one
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            # add the new max
            dq.append(i)
            res.append(nums[dq[0]])

        return res