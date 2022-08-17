from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_find_min1(self):
        x = Solution()
        self.assertEqual(1, x.findMin([1,3,5]))

    def test_find_min2(self):
        x = Solution()
        self.assertEqual(0, x.findMin([2,2,2,0,1]))

    def test_find_min3(self):
        x = Solution()
        self.assertEqual(-1, x.findMin([2,2,2,-1,0,1]))

    def test_find_min4(self):
        x = Solution()
        self.assertEqual(1, x.findMin([1,1]))

    def test_find_min5(self):
        x = Solution()
        self.assertEqual(-10, x.findMin([3,4,4,4,4,4,4,5,5,6,6,6,6,6,6,6,7,7,7,7,7,7,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,10,10,10,-10,-10,-10,-9,-8,-8,-8,-8,-8,-7,-7,-7,-7,-6,-6,-6,-6,-6,-6,-6,-5,-5,-5,-4,-4,-4,-4,-3,-3,-3,-3,-3,-3,-2,-2,-2,-2,-1,-1,0,0,0,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3]))

    def test_find_min6(self):
        x = Solution()
        self.assertEqual(1, x.findMin([1,1,1]))

    def test_find_min7(self):
        x = Solution()
        self.assertEqual(1, x.findMin([3,1,1]))
