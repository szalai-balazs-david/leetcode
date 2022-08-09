from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_min_path_sum1(self):
        x = Solution()
        input = [[1,3,1],[1,5,1],[4,2,1]]
        self.assertEqual(7, x.minPathSum(input))

    def test_min_path_sum2(self):
        x = Solution()
        input = [[1,2,3],[4,5,6]]
        self.assertEqual(12, x.minPathSum(input))
