class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if n == 1:
            return s
        res =  "" 
        resLen = 0

        # n times
        for i in range(n):
            # odd length
            l,r = i,i
            # O(n)
            while l>=0 and r<len(s) and s[l] == s[r]:
                if resLen < r-l+1:
                    res = s[l:r+1]
                    resLen = r-l+1
                l-=1
                r+=1
            # even length
            l,r = i,i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                if resLen < r-l+1:
                    res = s[l:r+1]
                    resLen = r-l+1
                l-=1
                r+=1
        
        return res