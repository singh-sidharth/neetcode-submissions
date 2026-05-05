class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # brute force way
        # generate all subtstrings
        # see if substrings match

        memo = {}
        memo[len(s)] = True
        #loop through string (stargint index is the state variable)
        def dfs(i):
            if i in memo:
                return memo[i]
            for w in wordDict:
                if ((i + len(w)) <= len(s) and 
                     s[i : i + len(w)] == w
                ):
                    if dfs(i + len(w)):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        
        return dfs(0)