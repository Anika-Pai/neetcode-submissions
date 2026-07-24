class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = { ')' : '(',
                    ']' : '[',
                    '}' : '{' }

        if len(s) % 2 != 0:
            return False

        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            
            if c == ')' or c == ']' or c == '}':
                if not stack:
                    return False
                popped = stack.pop()

                if popped != matches[c]:
                    return False
        
        if stack:
            return False
        
        return True