class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        if n == 0:
            return [""]
        result = []

        for i in range(n):
            left = self.generateParenthesis(n - 1 - i)
            right = self.generateParenthesis(i)
            for l in left:
                for r in right:
                    result.append(f"({l}){r}")

        return result
