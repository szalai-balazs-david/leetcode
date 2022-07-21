from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_plus_one1(self):
        x = Solution()
        self.assertListEqual([1,2,4], x.plusOne([1,2,3]))

    def test_plus_one2(self):
        x = Solution()
        self.assertListEqual([4,3,2,2], x.plusOne([4,3,2,1]))

    def test_plus_one3(self):
        x = Solution()
        self.assertListEqual([1,0], x.plusOne([9]))
