class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        if len(s) % 2 != 0:
            return False

        for char in s:
            if char in ('{', '(', '['):
                stack.append(char)
            else:
                if not stack:
                    return False
                
                open_char = stack.pop()
                if open_char != match[char]:
                    return False
        
        return len(stack) == 0
