class Solution:
    # def __init__(self):
    #     self.ch = [0] * 26

    # def isAnagram(self, s: str) -> bool:

    #     currentCount = [0] * 26
    #     for i in s:
    #         currentCount[ord(i) - ord("a")] += 1

    #     return currentCount == self.ch

    #     return True

    # def checkInclusion(self, s1: str, s2: str) -> bool:
    #     length_s1 = len(s1)
    #     length_s2 = len(s2)

    #     if length_s1 > length_s2:
    #         return False
    #     # Initialize character counts for permutation check
    #     for i in s1:
    #         self.ch[ord(i) - ord("a")] += 1

    #     # The window length is length_s1.
    #     l = 0
    #     for r, char in enumerate(s2, length_s1):
    #         if self.isAnagram(s2[l:r]):
    #             return True
    #         l += 1

    #     return False
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length_s1 = len(s1)
        length_s2 = len(s2)

        if length_s1 > length_s2:
            return False

        count_s1 = [0] * 26
        count_s2 = [0] * 26
        # Initialize character counts for permutation check
        for i in range(length_s1):
            count_s1[ord(s1[i]) - ord("a")] += 1
            count_s2[ord(s2[i]) - 97] += 1

        # The window length is length_s1.
        for left in range(length_s2 - length_s1):
            if count_s1 == count_s2:
                return True
            count_s2[ord(s2[left]) - 97] -= 1
            count_s2[ord(s2[left + length_s1]) - 97] += 1

        return count_s1 == count_s2