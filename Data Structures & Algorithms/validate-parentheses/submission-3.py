class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        if len(s) % 2 != 0:
            return False

        for char in s:
            if char in ('{', '(', '['):
                stack.append(char)
            
            if char == '}':
                if not stack:
                    return False
                open_char = stack.pop()
                if (open_char != '{'):
                    return False
            if char == ')':
                if not stack:
                    return False
                open_char = stack.pop()
                if (open_char != '('):
                    return False
            if char == ']':
                if not stack:
                    return False
                open_char = stack.pop()
                if (open_char != '['):
                    return False
        
        return len(stack) == 0
