from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_combinationSum1(self):
        x = Solution()
        expected = [[2,2,3],[7]]
        actual = x.combinationSum([2,3,6,7], 7)
        self.assertEqual(len(expected), len(actual))
        for i in range(len(actual)):
            self.assertTrue(actual[i] in expected)

    def test_combinationSum2(self):
        x = Solution()
        expected = [[2,2,2,2],[2,3,3],[3,5]]
        actual = x.combinationSum([2,3,5], 8)
        self.assertEqual(len(expected), len(actual))
        for i in range(len(actual)):
            self.assertTrue(actual[i] in expected)

    def test_combinationSum3(self):
        x = Solution()
        expected = []
        actual = x.combinationSum([2], 1)
        self.assertEqual(len(expected), len(actual))
        for i in range(len(actual)):
            self.assertTrue(actual[i] in expected)

    def test_combinationSum4(self):
        #testing for timeout
        x = Solution()
        x.combinationSum([4, 12, 100, 200], 400)
