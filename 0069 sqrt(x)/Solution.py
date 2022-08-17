class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x
        mid = (l + r) // 2
        while l < r - 1:
            mid = (l + r) // 2
            square = mid * mid
            if square == x:
                return mid
            if square < x:
                l = mid
            else:
                r = mid
        return mid if mid * mid <= x else mid - 1
