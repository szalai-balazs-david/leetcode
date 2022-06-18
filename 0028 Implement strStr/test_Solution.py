from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_strStr1(self):
        x = Solution()
        self.assertEqual(2, x.strStr("hello", "ll"))

    def test_strStr2(self):
        x = Solution()
        self.assertEqual(-1, x.strStr("aaaaa", "bba"))
