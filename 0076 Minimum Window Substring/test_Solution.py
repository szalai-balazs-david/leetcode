from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_min_window1(self):
        x = Solution()
        self.assertEqual("BANC", x.minWindow("ADOBECODEBANC", "ABC"))

    def test_min_window2(self):
        x = Solution()
        self.assertEqual("a", x.minWindow("a", "a"))

    def test_min_window3(self):
        x = Solution()
        self.assertEqual("", x.minWindow("a", "aa"))
