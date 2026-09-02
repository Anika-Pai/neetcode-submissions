class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        length = len(s)

        if length % 2 != 0:
            return False

        for c in s:
            if (c == '(' or
                c == '{' or
                c == '['):
                st.append(c)
            elif not st:
                return False
            elif (c == ')' and st.pop() != '(') :
                return False
            elif (c == '}' and st.pop() != '{'):
                return False
            elif (c == ']' and st.pop() != '['):
                return False
            else:
                continue
        
        return len(st) == 0