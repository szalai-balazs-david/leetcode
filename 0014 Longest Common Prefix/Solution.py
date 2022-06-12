class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        result = ""

        shortest = len(strs[0])
        for s in strs[1:]:
            shortest = min(shortest, len(s))

        for i in range(shortest):
            c = strs[0][i]
            good = True
            for s in strs[1:]:
                if s[i] != c:
                    good = False
                    break
            if good:
                result += c
            else:
                break

        return result
