from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_can_jump1(self):
        x = Solution()
        self.assertEqual(True, x.canJump([2,3,1,1,4]))

    def test_can_jump2(self):
        x = Solution()
        self.assertEqual(False, x.canJump([3,2,1,0,4]))

    def test_can_jump3(self):
        x = Solution()
        self.assertEqual(True, x.canJump([0]))

    def test_can_jump4(self):
        x = Solution()
        self.assertEqual(False, x.canJump([0,1]))

    def test_can_jump5(self):
        x = Solution()
        self.assertEqual(True, x.canJump([2,3,1,1,4,0]))
