from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_add_binary1(self):
        x = Solution()
        self.assertEqual("100", x.addBinary("11", "1"))

    def test_add_binary2(self):
        x = Solution()
        self.assertEqual("10101", x.addBinary("1010", "1011"))
