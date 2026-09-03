class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = "".join(c.lower() for c in s if c.isalnum())
        return lower == lower[::-1]