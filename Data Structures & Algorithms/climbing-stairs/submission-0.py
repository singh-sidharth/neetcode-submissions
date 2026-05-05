class Solution:
    def climbStairs(self, n: int) -> int:

        first = 1
        second = 2

        if n==0 or n ==1:
            return first
        if n==2:
            return second
        third = 0
        # 1 stair: 1 way
        # 2 stairs: 2 ways
        # 3 stairs {[1,2], [2,1],[1,1,1]}
        # 4 startis {[1,2,1],[2,2], [2,1,1],[1,1,2], [1,1,1,1]}

        for i in range(3,n+1):
            third = first + second
            first = second
            second = third

        return third