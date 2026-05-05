class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        if not strs:
            return ""

        for s in strs:
            res+= str(len(s))+'#'+s
        
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        res,i = [], 0
        while i < len(s):
            j = i
            # find the length of string encoded in it
            while s[j] != '#':
                j += 1
            length = int(s[i:j])

            # use this length to decode string
            # traverse the string
            j+=1
            i = j
            while i < (j+length):
                i +=1

            res.append(s[j:i])
        
        return res