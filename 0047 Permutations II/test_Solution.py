from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_permute_unique1(self):
        x = Solution()
        expected = [[1,1,2], [1,2,1], [2,1,1]]
        actual = x.permuteUnique([1,1,2])
        self.assertEqual(len(expected), len(actual))
        for ex in expected:
            self.assertTrue(ex in actual)

    def test_permute_unique2(self):
        x = Solution()
        expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        actual = x.permuteUnique([1,2,3])
        self.assertEqual(len(expected), len(actual))
        for ex in expected:
            self.assertTrue(ex in actual)
