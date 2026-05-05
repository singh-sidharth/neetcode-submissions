class Solution:
    def __init__(self):
        self.ch = [0] * 26

    def isAnagram(self, s: str) -> bool:

        currentCount = [0] * 26
        for i in s:
            currentCount[ord(i) - ord("a")] += 1

        return currentCount == self.ch

        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        length_s1 = len(s1)
        length_s2 = len(s2)

        if length_s1 > length_s2:
            return False
        # Initialize character counts for permutation check
        for i in s1:
            self.ch[ord(i) - ord("a")] += 1

        # The window length is length_s1.
        l = 0
        for r, char in enumerate(s2, length_s1):
            if self.isAnagram(s2[l:r]):
                return True
            l += 1

        return False
        