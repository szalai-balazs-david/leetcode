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

    def test_searchInsert4(self):
        x = Solution()
        self.assertEqual(7, x.searchInsert([1,3,5,6,8,9,100], 101))

    def test_searchInsert5(self):
        x = Solution()
        self.assertEqual(0, x.searchInsert([1,3,5,6,8,9,100], 0))

    def test_searchInsert6(self):
        x = Solution()
        self.assertEqual(0, x.searchInsert([1], 0))

    def test_searchInsert7(self):
        x = Solution()
        self.assertEqual(0, x.searchInsert([1], 1))

    def test_searchInsert8(self):
        x = Solution()
        self.assertEqual(1, x.searchInsert([1], 2))

    def test_searchInsert9(self):
        x = Solution()
        self.assertEqual(1, x.searchInsert([1,3], 3))
