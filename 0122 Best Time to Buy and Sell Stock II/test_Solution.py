from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_max_profit1(self):
        x = Solution()
        self.assertEqual(7, x.maxProfit([7,1,5,3,6,4]))

    def test_max_profit2(self):
        x = Solution()
        self.assertEqual(4, x.maxProfit([1,2,3,4,5]))

    def test_max_profit3(self):
        x = Solution()
        self.assertEqual(0, x.maxProfit([7,6,4,3,1]))
