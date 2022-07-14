from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_max_sub_array1(self):
        x = Solution()
        self.assertEqual(6, x.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

    def test_max_sub_array2(self):
        x = Solution()
        self.assertEqual(1, x.maxSubArray([1]))

    def test_max_sub_array3(self):
        x = Solution()
        self.assertEqual(23, x.maxSubArray([5,4,-1,7,8]))
