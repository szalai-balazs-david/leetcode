from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_search_matrix1(self):
        x = Solution()
        self.assertEqual(True, x.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))

    def test_search_matrix2(self):
        x = Solution()
        self.assertEqual(False, x.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))

    def test_search_matrix3(self):
        x = Solution()
        self.assertEqual(True, x.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 1))

    def test_search_matrix4(self):
        x = Solution()
        self.assertEqual(True, x.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 5))

    def test_search_matrix5(self):
        x = Solution()
        self.assertEqual(True, x.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 5))

    def test_search_matrix6(self):
        x = Solution()
        self.assertEqual(False, x.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 0))

    def test_search_matrix7(self):
        x = Solution()
        self.assertEqual(False, x.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 61))
