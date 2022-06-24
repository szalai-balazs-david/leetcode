from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_jump1(self):
        x = Solution()
        self.assertEqual(2, x.jump([2,3,1,1,4]))

    def test_jump2(self):
        x = Solution()
        self.assertEqual(2, x.jump([2,3,0,1,4]))

    def test_jump3(self):
        x = Solution()
        self.assertEqual(6, x.jump([2,3,0,1,4,1,3,2,1,2,1,3,2,4,1]))

    def test_jump4(self):
        x = Solution()
        self.assertEqual(0, x.jump([0]))
