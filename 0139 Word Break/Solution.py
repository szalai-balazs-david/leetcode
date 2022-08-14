class Solution:
    #Cheated: looked up solution, then implemented it
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        max_len = 0
        for word in wordDict:
            max_len = max(max_len, len(word))

        ok = [True]
        for i in range(1, len(s) + 1):
            current = False
            for j in range(max(0, i-max_len), i):
                if ok[j] and s[j:i] in wordDict:
                    current = True
                    break
            ok.append(current)
        return ok[-1]
