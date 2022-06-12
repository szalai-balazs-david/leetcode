from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_reverse1(self):
        x = Solution()
        self.assertEqual(123, x.reverse(321))

    def test_reverse2(self):
        x = Solution()
        self.assertEqual(-123, x.reverse(-321))

    def test_reverse3(self):
        x = Solution()
        self.assertEqual(21, x.reverse(120))

    def test_reverse4(self):
        x = Solution()
        self.assertEqual(0, x.reverse(1534236469))
