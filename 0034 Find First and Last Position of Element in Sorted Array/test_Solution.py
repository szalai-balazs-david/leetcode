from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_searchRange1(self):
        x = Solution()
        self.assertListEqual([3, 4], x.searchRange([5,7,7,8,8,10], 8))

    def test_searchRange2(self):
        x = Solution()
        self.assertListEqual([-1, -1], x.searchRange([5,7,7,8,8,10], 6))

    def test_searchRange3(self):
        x = Solution()
        self.assertListEqual([-1, -1], x.searchRange([], 0))
