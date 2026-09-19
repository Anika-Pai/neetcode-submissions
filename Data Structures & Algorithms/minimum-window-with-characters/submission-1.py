class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        required_counts = Counter(t)
        window_counts = {}

        need = len(required_counts)
        have = 0

        l = 0
        best_start = 0
        best_length = float("inf")

        for r in range(len(s)):
            window_counts[s[r]] = window_counts.get(s[r], 0) + 1

            if (s[r] in required_counts
                and window_counts[s[r]] == required_counts[s[r]]):
                have += 1

            while have == need:

                if r - l + 1 < best_length:
                    best_start = l
                    best_length = r - l + 1

                window_counts[s[l]] -= 1

                if (s[l] in required_counts and 
                    window_counts[s[l]] < required_counts[s[l]]):
                    have -= 1

                l += 1

        if best_length == float("inf"):
            return ""

        return s[best_start:best_start + best_length]
            

