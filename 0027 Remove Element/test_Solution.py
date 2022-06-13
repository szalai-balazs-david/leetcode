from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_removeElement1(self):
        x = Solution()
        nums = [3,2,2,3]
        expected = [2,2]
        count = x.removeElement(nums, 3)
        self.assertEqual(len(expected), count)
        self.assertEqual(len(expected), len(nums))
        for i in range(len(expected)):
            self.assertEqual(expected[i], nums[i])

    def test_removeElement2(self):
        x = Solution()
        nums = [0,1,2,2,3,0,4,2]
        expected = [0,1,3,0,4]
        count = x.removeElement(nums, 2)
        self.assertEqual(len(expected), count)
        self.assertEqual(len(expected), len(nums))
        for i in range(len(expected)):
            self.assertEqual(expected[i], nums[i])
