class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False

        st = []
        
        st.append(s[0])
        for i in range(1, len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                st.append(s[i])
            elif s[i] == ')':
                if len(st) == 0:
                    return False
                if st[-1] != '(':
                    return False
                st.pop()
            elif s[i] == '}':
                if len(st) == 0:
                    return False
                if st[-1] != '{':
                    return False
                st.pop()
            elif s[i] == ']':
                if len(st) == 0:
                    return False
                if st[-1] != '[':
                    return False
                st.pop()

        return len(st) == 0