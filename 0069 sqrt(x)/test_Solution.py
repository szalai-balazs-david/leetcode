from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_my_sqrt1(self):
        x = Solution()
        self.assertEqual(1, x.mySqrt(1))

    def test_my_sqrt2(self):
        x = Solution()
        self.assertEqual(1, x.mySqrt(2))

    def test_my_sqrt3(self):
        x = Solution()
        self.assertEqual(1, x.mySqrt(3))

    def test_my_sqrt4(self):
        x = Solution()
        self.assertEqual(2, x.mySqrt(4))

    def test_my_sqrt5(self):
        x = Solution()
        self.assertEqual(2, x.mySqrt(8))

    def test_my_sqrt6(self):
        x = Solution()
        self.assertEqual(4, x.mySqrt(20))
