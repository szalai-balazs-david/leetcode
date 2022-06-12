from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_meth1(self):
        x = Solution()
        self.assertEqual("III", x.intToRoman(3))

    def test_meth2(self):
        x = Solution()
        self.assertEqual("LVIII", x.intToRoman(58))

    def test_meth3(self):
        x = Solution()
        self.assertEqual("MCMXCIV", x.intToRoman(1994))
