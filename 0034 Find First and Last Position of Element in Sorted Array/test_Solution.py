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

    def test_searchRange4(self):
        x = Solution()
        self.assertListEqual([6,6], x.searchRange([1,3,7,7,8,8,10,11], 10))

    def test_searchRange5(self):
        x = Solution()
        self.assertListEqual([2,5], x.searchRange([1,2,3,3,3,3,4,5,9],3))
