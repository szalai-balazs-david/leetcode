class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) % 2 == 1:
            return False

        old = len(s)
        new = 0
        while new != old and len(s) != 0:
            old = len(s)
            s = s.replace("()", "")
            s = s.replace("[]", "")
            s = s.replace("{}", "")
            new = len(s)

        if len(s) == 0:
            return True
        return False
