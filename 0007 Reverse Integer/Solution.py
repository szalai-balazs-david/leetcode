class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        negative = x < 0
        x = abs(x)
        while x != 0:
            result = result * 10 + x % 10
            x = int(x / 10)
        if negative:
            result = -1 * result
        return 0 if result < -1 * (2 ** 31) or result > 2 ** 31 - 1 else result
