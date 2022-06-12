class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits) == 0:
            return []
        dict = {"2": "abc","3": "def","4": "ghi","5": "jkl","6": "mno","7": "pqrs","8": "tuv","9": "wxyz",}
        result = []

        def dfs(result, string):
            if len(string) == len(digits):
                result.append(string)
            else:
                for c in dict[digits[len(string)]]:
                    dfs(result, string + c)

        dfs(result, "")
        return result
