class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mp = {}
        for i in s:
            mp[i] = mp.get(i, 0) + 1
        
        for c in t:
            if c not in mp:
                return False
            mp[c] -= 1
            if mp[c] < 0:
                return False
        
        return True