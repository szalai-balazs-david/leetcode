from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_makesquare1(self):
        x = Solution()
        self.assertEqual(True, x.makesquare([1,1,2,2,2]))

    def test_makesquare2(self):
        x = Solution()
        self.assertEqual(False, x.makesquare([3,3,3,3,4]))

    def test_makesquare3(self):
        x = Solution()
        self.assertEqual(True, x.makesquare([5,5,5,5,4,4,4,4,3,3,3,3]))

    def test_makesquare4(self):
        x = Solution()
        self.assertEqual(True, x.makesquare([13,11,1,8,6,7,8,8,6,7,8,9,8]))

    def test_makesquare5(self):
        x = Solution()
        self.assertEqual(False, x.makesquare([14,10,10,10,10,10,10,10,10,10,10,10,8,9,19]))
