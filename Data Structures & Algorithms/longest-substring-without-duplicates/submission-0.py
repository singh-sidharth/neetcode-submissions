class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        memo = defaultdict(int)
        res = 0
        i = 0
        j = 0
        n = len(s)
        count = 0

        while i <= j and j < n:
            if s[j] not in memo:
                memo[s[j]] = j

            else:
                # Get the index of previously seen element
                tempIdx = memo[s[j]]

                # check if it is a part of current sub string
                if tempIdx >= i:
                    # iterate till that element is not present anymore
                    while tempIdx < j and s[tempIdx] == s[j]:
                        tempIdx += 1

                    # store the new result before storing the index
                    count = j - i
                    res = res if res >= count else count

                    # reset the start position and continue counting for new substrings
                    i = tempIdx
                # update the new index into memo
                memo[s[j]] = j

            count = j - i + 1
            j += 1

        res = res if res >= count else count
        return res