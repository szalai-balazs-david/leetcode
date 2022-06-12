from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_longestCommonPrefix1(self):
        x = Solution()
        self.assertEqual("fl", x.longestCommonPrefix(["flower","flow","flight"]))

    def test_longestCommonPrefix2(self):
        x = Solution()
        self.assertEqual("", x.longestCommonPrefix(["dog","racecar","car"]))

    def test_longestCommonPrefix3(self):
        x = Solution()
        self.assertEqual("c", x.longestCommonPrefix(["cir","car"]))
