class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        maxfreq = 0
        counts = {}
        res = 0

        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            maxfreq = max(maxfreq, counts[s[r]])

            while (r - l + 1) - maxfreq > k:
                counts[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res


        

