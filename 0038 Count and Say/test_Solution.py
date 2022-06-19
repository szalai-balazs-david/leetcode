from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_countAndSay1(self):
        x = Solution()
        self.assertEqual("1", x.countAndSay(1))

    def test_countAndSay2(self):
        x = Solution()
        self.assertEqual("1211", x.countAndSay(4))

    def test_countAndSay3(self):
        x = Solution()
        self.assertEqual("111221", x.countAndSay(5))
