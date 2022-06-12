from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_convert1(self):
        x = Solution()
        self.assertEqual("PAHNAPLSIIGYIR", x.convert("PAYPALISHIRING", 3))

    def test_convert2(self):
        x = Solution()
        self.assertEqual("AGMBFHLNCEIKDJ", x.convert("ABCDEFGHIJKLMN", 4))

    def test_convert3(self):
        x = Solution()
        self.assertEqual("A", x.convert("A", 1))
