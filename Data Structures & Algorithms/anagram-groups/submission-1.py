class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ansMap = defaultdict(list)

        for s in strs:
            mem = [0]*26
            for c in s:
                mem[ord(c) - ord('a')] +=1
            key = tuple(mem)
            ansMap[key].append(s)
        
        return list(ansMap.values())
