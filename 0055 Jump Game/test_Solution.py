from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_can_jump1(self):
        x = Solution()
        self.assertEqual(True, x.canJump([2,3,1,1,4]))

    def test_can_jump2(self):
        x = Solution()
        self.assertEqual(False, x.canJump([3,2,1,0,4]))
