from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_my_atoi1(self):
        x = Solution()
        self.assertEqual(42, x.myAtoi("42"))

    def test_my_atoi2(self):
        x = Solution()
        self.assertEqual(42, x.myAtoi("  42"))

    def test_my_atoi3(self):
        x = Solution()
        self.assertEqual(-42, x.myAtoi("  -42"))

    def test_my_atoi3(self):
        x = Solution()
        self.assertEqual(0, x.myAtoi("+-42"))
