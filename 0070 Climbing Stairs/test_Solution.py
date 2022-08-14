from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_climb_stairs1(self):
        x = Solution()
        self.assertEqual(2, x.climbStairs(2))

    def test_climb_stairs2(self):
        x = Solution()
        self.assertEqual(3, x.climbStairs(3))

    def test_climb_stairs3(self):
        x = Solution()
        self.assertEqual(5, x.climbStairs(4))

    def test_climb_stairs4(self):
        x = Solution()
        print(x.climbStairs(38))
