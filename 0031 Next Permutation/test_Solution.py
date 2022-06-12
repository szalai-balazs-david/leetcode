from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_nextPermutation1(self):
        nums = [1, 2, 3]
        expected = [1,3,2]
        x = Solution()
        x.nextPermutation(nums)
        self.assertListEqual(expected, nums)

    def test_nextPermutation2(self):
        nums = [3,2,1]
        expected = [1,2,3]
        x = Solution()
        x.nextPermutation(nums)
        self.assertListEqual(expected, nums)

    def test_nextPermutation3(self):
        nums = [1, 1, 5]
        expected = [1,5,1]
        x = Solution()
        x.nextPermutation(nums)
        self.assertListEqual(expected, nums)

    def test_nextPermutation4(self):
        nums = [1, 3, 2]
        expected = [2,1,3]
        x = Solution()
        x.nextPermutation(nums)
        self.assertListEqual(expected, nums)

    def test_nextPermutation5(self):
        nums = [2, 3, 1]
        expected = [3,1,2]
        x = Solution()
        x.nextPermutation(nums)
        self.assertListEqual(expected, nums)
