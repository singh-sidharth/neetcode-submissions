# s.length = [1,1000]
# 'X' is minimum input
# k is replacement so treat them like they are the same character
# Question what does 'k' character mean. Does k inlcude or exclude duplicates?

# AABABBB
# A valid window will maintain k repeated sequences, else go to previous sequence
# which is windowSize - maxFreq = k

# Initialize: start = 0, seen = map(), 
# 
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        seen = {}
        l=0
        answer = 0

        for r,ch in enumerate(s):
            seen[ch]= 1 + seen.get(ch,0)
            windowSize = r-l+1

            tempK = windowSize - max(seen.values())

            if tempK > k and l<=r:
                seen[s[l]] -= 1
                l += 1
            
            answer = max(answer, r-l+1)

        return answer