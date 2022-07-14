from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_reverse_bits1(self):
        x = Solution()
        self.assertEqual(964176192, x.reverseBits(43261596))

    def test_reverse_bits2(self):
        x = Solution()
        self.assertEqual(3221225471, x.reverseBits(4294967293))
