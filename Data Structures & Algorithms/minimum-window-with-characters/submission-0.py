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
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1

            if (
                char in required_counts
                and window_counts[char] == required_counts[char]
            ):
                have += 1

            while have == need:
                window_length = r - l + 1

                if window_length < best_length:
                    best_start = l
                    best_length = window_length

                left_char = s[l]
                window_counts[left_char] -= 1

                if (
                    left_char in required_counts
                    and window_counts[left_char] < required_counts[left_char]
                ):
                    have -= 1

                l += 1

        if best_length == float("inf"):
            return ""

        return s[best_start:best_start + best_length]
            

