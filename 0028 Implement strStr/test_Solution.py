from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_strStr1(self):
        x = Solution()
        self.assertEqual(2, x.strStr("hello", "ll"))

    def test_strStr2(self):
        x = Solution()
        self.assertEqual(-1, x.strStr("aaaaa", "bba"))

    def test_strStr3(self):
        x = Solution()
        self.assertEqual(-1, x.strStr("mississippi", "issipi"))

    def test_strStr4(self):
        x = Solution()
        self.assertEqual(-1, x.strStr("issipi", "mississippi"))

    def test_strStr5(self):
        x = Solution()
        self.assertEqual(0, x.strStr("aaaaaa", ""))
