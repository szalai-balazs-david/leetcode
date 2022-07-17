class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        result = 0
        if m >= 2:
            result += self.uniquePaths(m-1, n)
        if n >= 2:
            result += self.uniquePaths(m, n-1)
        return result
