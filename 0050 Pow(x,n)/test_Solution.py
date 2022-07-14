from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_my_pow1(self):
        x = Solution()
        self.assertEqual(1024, x.myPow(2, 10))

    def test_my_pow2(self):
        x = Solution()
        self.assertEqual(9.261, x.myPow(2.1, 3))

    def test_my_pow3(self):
        x = Solution()
        self.assertEqual(0.25, x.myPow(2, -2))

    def test_my_pow4(self):
        x = Solution()
        self.assertEqual(0, x.myPow(0.00001,2147483647))

    def test_my_pow5(self):
        x = Solution()
        self.assertEqual(pow(34.00515,-3), x.myPow(34.00515,-3))
