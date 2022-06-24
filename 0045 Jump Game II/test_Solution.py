from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_jump1(self):
        x = Solution()
        self.assertEqual(2, x.jump([2,3,1,1,4]))

    def test_jump2(self):
        x = Solution()
        self.assertEqual(2, x.jump([2,3,0,1,4]))
