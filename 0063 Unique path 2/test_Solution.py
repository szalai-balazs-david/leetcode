from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_unique_paths_with_obstacles1(self):
        x = Solution()
        self.assertEqual(2, x.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))

    def test_unique_paths_with_obstacles2(self):
        x = Solution()
        self.assertEqual(1, x.uniquePathsWithObstacles([[0,1],[0,0]]))
