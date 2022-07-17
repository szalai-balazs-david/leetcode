from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_unique_paths1(self):
        x = Solution()
        self.assertEqual(28, x.uniquePaths(3, 7))

    def test_unique_paths2(self):
        x = Solution()
        self.assertEqual(3, x.uniquePaths(3, 2))
