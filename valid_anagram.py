# a python that checks if two strings are anagrams of each other

def valid_anagram(s, t):
    if len(s) != len(t):
        return False
    s_dict = {}
    t_dict = {}
    for i in range(len(s)):
        if s[i] in s_dict:
            s_dict[s[i]] += 1
        else:
            s_dict[s[i]] = 1
        if t[i] in t_dict:
            t_dict[t[i]] += 1
        else:
            t_dict[t[i]] = 1
    for key in s_dict:
        if key not in t_dict:
            return False
        if s_dict[key] != t_dict[key]:
            return False
    return True


    ###solution 2

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return Counter(s) == Counter(t)

        #return sorted(s) == sorted(t)
        
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1+ countS.get(s[i],0)
            countT[t[i]] = 1+ countT.get(t[i],0)

        for c in countS:
            if countS[c] != countT.get(c,0):
                return False

        return True