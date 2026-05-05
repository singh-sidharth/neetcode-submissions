class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == 0:
            return 0
        
        n = len(s)
        
        dp = {n: 1}

        for i in range(n-1, -1, -1):
            # no of decoding startin from 0 is 0
            # it is invalid
            if s[i] == '0':
                dp[i] = 0
            # no of ways if consider 1 digit
            else:
                dp[i] = dp[i+1]
            # no of ways if i consider 2 digit numberer
            if i+1 < n and (s[i] == '1'or s[i]=='2' and s[i+1] in '0123456'):
                dp[i] += dp[i+2]
        
        return dp[0]
        

