class Solution:
    def isPalindrome(self, s: str) -> bool:
        prev = sorted(s)
        cleaned = ""

        for c in s:
            if c.isalnum():
                cleaned += c.lower()
        
        return cleaned == cleaned[::-1]