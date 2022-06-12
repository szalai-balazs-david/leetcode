class Solution:
    # Start: 7:07
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend > 0) == (divisor > 0)
        divisor = abs(divisor)
        dividend = abs(dividend)

        result = 0
        for i in range(31, -1, -1):
            if (dividend >> i) >= divisor:
                result = result + (1 << i)
                dividend = dividend - (divisor << i)

        result = result if positive else -result

        if result > 2**31 - 1:
            result = 2**31 - 1
        elif result < -(2**31):
            result = -(2**31)

        return result
