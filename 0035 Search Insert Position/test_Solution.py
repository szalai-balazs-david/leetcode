from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_searchInsert1(self):
        x = Solution()
        self.assertEqual(2, x.searchInsert([1,3,5,6], 5))

    def test_searchInsert2(self):
        x = Solution()
        self.assertEqual(1, x.searchInsert([1,3,5,6], 2))

    def test_searchInsert3(self):
        x = Solution()
        self.assertEqual(4, x.searchInsert([1,3,5,6], 7))
