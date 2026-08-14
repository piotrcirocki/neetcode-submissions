class Solution:
    def isAnagram(self, s: str, t: str) -> bool: 
        dict_s = {}
        dict_t = {}
        if len(s) != len(t):
            return False
        for i, x in enumerate(s):
            if x in dict_s:
                dict_s[x] += 1
            else:
                dict_s[x] = 1
        for i, x in enumerate(t):
            if x in dict_t:
                dict_t[x] += 1
            else:
                dict_t[x] = 1
        return (dict_s == dict_t)




