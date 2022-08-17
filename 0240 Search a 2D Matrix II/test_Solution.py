from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_search_matrix1(self):
        x = Solution()
        self.assertEqual(True, x.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))

    def test_search_matrix2(self):
        x = Solution()
        self.assertEqual(False, x.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20))

    def test_search_matrix3(self):
        x = Solution()
        self.assertEqual(False, x.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22]], 20))

    def test_search_matrix4(self):
        x = Solution()
        self.assertEqual(False, x.searchMatrix([[1,4,7],[2,5,8],[3,6,9],[10,13,14],[18,21,23]], 20))

    def test_search_matrix5(self):
        x = Solution()
        self.assertEqual(True, x.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22]], 19))

    def test_search_matrix6(self):
        x = Solution()
        self.assertEqual(True, x.searchMatrix([[1,4,7],[2,5,8],[3,6,9],[10,13,14],[18,21,23]], 21))

    def test_search_matrix7(self):
        x = Solution()
        self.assertEqual(False, x.searchMatrix([[1,4],[2,5]],3))

    def test_search_matrix8(self):
        x = Solution()
        self.assertEqual(True, x.searchMatrix([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]],15))
