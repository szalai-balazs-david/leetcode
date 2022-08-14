from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_climb_stairs1(self):
        x = Solution()
        self.assertEqual(2, x.climbStairs(2))

    def test_climb_stairs2(self):
        x = Solution()
        self.assertEqual(3, x.climbStairs(3))
