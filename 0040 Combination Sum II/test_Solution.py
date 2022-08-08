from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_combination_sum2_1(self):
        x = Solution()
        expected = [[2,2]]
        actual = x.combinationSum2([2,5,2,2], 4)
        self.assertEqual(len(expected), len(actual))
        for ex in expected:
            self.assertTrue(ex in actual)

    def test_combination_sum2_2(self):
        x = Solution()
        expected = [[1,1,6], [1,2,5], [1,7], [2,6]]
        actual = x.combinationSum2([10,1,2,7,6,1,5], 8)
        print(actual)
        self.assertEqual(len(expected), len(actual))
        for ex in expected:
            self.assertTrue(ex in actual)

    def test_combination_sum2_3(self):
        x = Solution()
        expected = [[1,2,2], [5]]
        actual = x.combinationSum2([2,5,2,1,2], 5)
        print(actual)
        self.assertEqual(len(expected), len(actual))
        for ex in expected:
            self.assertTrue(ex in actual)
