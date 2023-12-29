class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        for i in range(len(s)):
            if i != len(s):
                if s[i] == '(' and s[i+1] == ')':
                    s.pop(s[i] and s[i+1])
                elif s[i] == '[' and s[i+1] == ']':
                    s.pop(s[i] and s[i+1])
                elif s[i] == '{' and s[i+1] == '}':
                    s.pop(s[i] and s[i+1])
        if not s:
            return False
