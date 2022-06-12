from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_threeSumClosest1(self):
        x = Solution()
        self.assertEqual(2, x.threeSumClosest([-1,2,1,-4], 1))

    def test_threeSumClosest2(self):
        x = Solution()
        self.assertEqual(0, x.threeSumClosest([0, 0, 0], 1))

    def test_threeSumClosest3(self):
        x = Solution()
        self.assertEqual(3, x.threeSumClosest([1, 1, 1, 1], 0))

    def test_threeSumClosest4(self):
        x = Solution()
        self.assertEqual(0, x.threeSumClosest([0,2,1,-3], 1))
