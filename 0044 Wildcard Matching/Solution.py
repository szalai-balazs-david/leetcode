class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        if not s:
            return not p or (p[0] == "*" and self.isMatch(s, p[1:]))

        if p[0] == "*":
            if len(p) > 1 and p[1] == "*":
                return self.isMatch(s, p[1:])
            return self.isMatch(s, p[1:]) or self.isMatch(s[1:], p)
        else:
            return bool(s) and p[0] in [s[0], "?"] and self.isMatch(s[1:], p[1:])
