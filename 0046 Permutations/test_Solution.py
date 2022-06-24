from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_permute1(self):
        x = Solution()
        expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        actual = x.permute([1,2,3])
        self.assertEqual(len(expected), len(actual))
        for x in expected:
            self.assertTrue(x in actual)

    def test_permute2(self):
        x = Solution()
        expected = [[0,1],[1,0]]
        actual = x.permute([0,1])
        self.assertEqual(len(expected), len(actual))
        for x in expected:
            self.assertTrue(x in actual)

    def test_permute3(self):
        x = Solution()
        expected = [[1]]
        actual = x.permute([1])
        self.assertEqual(len(expected), len(actual))
        for x in expected:
            self.assertTrue(x in actual)
