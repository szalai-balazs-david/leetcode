class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        if p == "*":
            return True

        c = p[0]
        if c == "*":
            # There's at least 1 more letter in p
            if p[1] == "*":
                match = self.isMatch(s, p[1:])
                return match
            if p[1] == "?":
                match = self.isMatch(s, p[1:]) or (len(s) > 0 and self.isMatch(s[1:], p))
                return match
            section = ""
            is_exact_section = True
            is_final_section = True
            for c in p[1:]:
                if c == "*":
                    is_final_section = False
                    break
                if c == "?":
                    is_final_section = False
                    is_exact_section = False
                    break
                section += c
            if is_final_section:
                return section == s[-len(section):]
            if section in s:
                i = s.index(section)
                if is_exact_section:
                    return self.isMatch(s[i + len(section):], p[1 + len(section):])
                return self.isMatch(s[i + len(section):], p[1 + len(section):]) or self.isMatch(s[i + 1:], p)
            return False
        else:
            if not s:
                return False
            is_match = p[0] in [s[0], "?"]
            match = is_match and self.isMatch(s[1:], p[1:])
            return match
