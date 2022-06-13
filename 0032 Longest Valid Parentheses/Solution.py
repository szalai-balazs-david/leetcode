class Solution:
    def longestValidParentheses(self, s: str) -> int:
        result = 0

        array = []
        for c in s:
            array.append(1 if c == "(" else -1)

        i = 0
        while i < len(s):
            current = [0]
            for j in range(i, len(array)):
                current.append(current[-1] + array[j])
                if current[-1] < 0:
                    break
            i += 1
            if -1 not in current:
                j = 1
                while j < len(current) and current[j] not in current[j+1:]:
                    j += 1
                    i += 1

            current.reverse()
            sub_result = len(current) - current.index(0) - 1
            result = max(result, sub_result)

        return result
