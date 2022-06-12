from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_divide1(self):
        x = Solution()
        self.assertEqual(3, x.divide(10, 3))

    def test_divide2(self):
        x = Solution()
        self.assertEqual(-2, x.divide(7, -3))

    def test_divide3(self):
        x = Solution()
        self.assertEqual(1, x.divide(1, 1))

    def test_divide4(self):
        x = Solution()
        self.assertEqual(2147483647, x.divide(-2147483648,-1))
