from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_unique_paths_with_obstacles1(self):
        x = Solution()
        self.assertEqual(2, x.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))

    def test_unique_paths_with_obstacles2(self):
        x = Solution()
        self.assertEqual(1, x.uniquePathsWithObstacles([[0,1],[0,0]]))

    def test_unique_paths_with_obstacles3(self):
        x = Solution()
        self.assertEqual(0, x.uniquePathsWithObstacles([[0,0],[0,1]]))

    def test_unique_paths_with_obstacles4(self):
        x = Solution()
        self.assertEqual(0, x.uniquePathsWithObstacles([[1,0],[0,0]]))

    def test_unique_paths_with_obstacles5(self):
        x = Solution()
        self.assertEqual(0, x.uniquePathsWithObstacles([[0,0],[1,1],[0,0]]))
