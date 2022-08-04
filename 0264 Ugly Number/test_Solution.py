from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_nth_ugly_number1(self):
        x = Solution()
        self.assertEqual(12, x.nthUglyNumber(10))

    def test_nth_ugly_number2(self):
        x = Solution()
        self.assertEqual(1, x.nthUglyNumber(1))
