from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_removeDuplicates1(self):
        x = Solution()
        expected = [1,2]
        nums = [1,1,2]
        k = x.removeDuplicates(nums)
        self.assertEqual(len(expected), k)
        for i in range(len(expected)):
            self.assertEqual(expected[i], nums[i])

    def test_removeDuplicates2(self):
        x = Solution()
        expected = [0,1,2,3,4]
        nums = [0,0,1,1,1,2,2,3,3,4]
        k = x.removeDuplicates(nums)
        self.assertEqual(len(expected), k)
        for i in range(len(expected)):
            self.assertEqual(expected[i], nums[i])
