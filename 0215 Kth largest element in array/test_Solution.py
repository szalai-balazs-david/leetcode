from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_find_kth_largest1(self):
        x = Solution()
        self.assertEqual(5, x.findKthLargest([3,2,1,5,6,4], 2))

    def test_find_kth_largest2(self):
        x = Solution()
        self.assertEqual(4, x.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
