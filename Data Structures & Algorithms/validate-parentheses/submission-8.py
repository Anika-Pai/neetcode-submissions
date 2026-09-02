class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        st = []

        for c in s:
            if c not in pairs:
                st.append(c)
            else:
                if not st or st.pop() != pairs[c]:
                    return False
        
        return len(st) == 0