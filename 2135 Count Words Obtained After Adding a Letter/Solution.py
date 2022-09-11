class Solution:
    def wordCount(self, startWords: list[str], targetWords: list[str]) -> int:
        for i in range(len(startWords)):
            startWords[i] = ''.join(sorted(startWords[i]))
        starters = set(startWords)
        for i in range(len(targetWords)):
            targetWords[i] = ''.join(sorted(targetWords[i]))
        result = 0
        for target in targetWords:
            for i in range(len(target)):
                if target[:i] + target[i + 1:] in starters:
                    result += 1
                    break
        return result
