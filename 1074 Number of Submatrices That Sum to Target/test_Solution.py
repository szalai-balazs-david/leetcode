from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_num_submatrix_sum_target1(self):
        x = Solution()
        self.assertEqual(4, x.numSubmatrixSumTarget([[0,1,0],[1,1,1],[0,1,0]], 0))

    def test_num_submatrix_sum_target2(self):
        x = Solution()
        self.assertEqual(4, x.numSubmatrixSumTarget([[0,1,0],[1,1,1],[0,1,0]], 4))

    def test_num_submatrix_sum_target3(self):
        x = Solution()
        self.assertEqual(5, x.numSubmatrixSumTarget([[-1,1],[1,-1]], 0))

    def test_num_submatrix_sum_target4(self):
        x = Solution()
        self.assertEqual(0, x.numSubmatrixSumTarget([[1]], 0))
