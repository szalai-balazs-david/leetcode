class Solution:
    def longestValidParentheses(self, s: str) -> int:
        array = [0]
        for i in range(1, len(s)):
            sub_result = 0
            if s[i] == ")":
                if s[i-1] == "(":
                    sub_result = (array[i-2] if i >= 2 else 0) + 2
                elif i - array[i-1] > 0 and s[i - array[i-1] - 1] == "(":
                    sub_result = array[i - 1] + (array[i - array[i - 1] - 2] if (i - array[i - 1]) >= 2 else 0) + 2

            array.append(sub_result)

        return max(array)

