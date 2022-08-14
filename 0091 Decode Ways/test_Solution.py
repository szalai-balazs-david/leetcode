from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_num_decodings1(self):
        x = Solution()
        self.assertEqual(2, x.numDecodings("12"))

    def test_num_decodings2(self):
        x = Solution()
        self.assertEqual(3, x.numDecodings("226"))

    def test_num_decodings3(self):
        x = Solution()
        self.assertEqual(0, x.numDecodings("06"))

    def test_num_decodings4(self):
        x = Solution()
        self.assertEqual(0, x.numDecodings("2260"))

    def test_num_decodings5(self):
        x = Solution()
        self.assertEqual(3, x.numDecodings("22620"))
