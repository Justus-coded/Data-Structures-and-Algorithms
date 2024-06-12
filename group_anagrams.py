from typing import List

strs = ["act","pots","tops","cat","stop","hat"]
# Output: [["act","cat"],["pots","tops","stop"],["hat"]]

# Given an array of strings, group anagrams together.
def groupAnagrams(strs):
    anagrams = {}
    for s in strs:
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            anagrams[sorted_s].append(s)
        else:
            anagrams[sorted_s] = [s]
    return list(anagrams.values())


print(groupAnagrams(strs))
## Solution 2
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {} #mapping charCount to a list of Anagrams

        for s in strs:
            charCount = [0]*26
            for c in s:
                charCount[ord(c)-ord('a')] += 1
            key = tuple(charCount)
            if key in res:
                res[key].append(s)
            else:
                res[key] = [s]
        return res.values()


print(Solution().groupAnagrams(strs))