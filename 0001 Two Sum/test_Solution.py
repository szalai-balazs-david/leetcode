from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_two_sum1(self):
        nums = [1, 2, 3]
        target = 5
        expected = [1, 2]
        x = Solution()
        actual = x.two_sum(nums, target)
        self.assertListEqual(actual, expected)

    def test_two_sum2(self):
        nums = [1, 2, 3]
        target = 6
        x = Solution()
        self.assertRaises(Exception, lambda: x.two_sum(nums, target))
