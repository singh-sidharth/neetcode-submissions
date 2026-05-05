class TimeMap:

    def __init__(self):
        self.memo = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.memo:
            self.memo[key] = []
        self.memo[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.memo:
            return ""

        if timestamp < self.memo[key][0][0]:
            return ""
        if timestamp >= self.memo[key][-1][0]:
            return self.memo[key][-1][1]

        left = 0

        right = len(self.memo[key])

        while left < right:
            mid = (left + right) // 2
            if self.memo[key][mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid

        # if iterator points to first element it means,
        # no time <=timestamp exists
        return "" if right == 0 else self.memo[key][right - 1][1]
        
