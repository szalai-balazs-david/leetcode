from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_solve_nqueens1(self):
        x = Solution()
        expected = [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
        actual = x.solveNQueens(4)
        self.assertEqual(len(expected), len(actual))
        for ex in expected:
            self.assertTrue(ex in actual)

    def test_solve_nqueens2(self):
        x = Solution()
        expected = [["Q"]]
        actual = x.solveNQueens(1)
        self.assertEqual(len(expected), len(actual))
        for ex in expected:
            self.assertTrue(ex in actual)
