from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_fourSum1(self):
        x = Solution()
        result = x.fourSum([1,0,-1,0,-2,2], 0)
        expected = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
        self.assertEqual(len(expected), len(result))
        for i in range(len(result)):
            res = result[i]
            res.sort()
            self.assertListEqual(expected[i], res)

    def test_fourSum2(self):
        x = Solution()
        result = x.fourSum([2,2,2,2,2,2], 8)
        expected = [[2,2,2,2]]
        self.assertEqual(len(expected), len(result))
        for i in range(len(result)):
            res = result[i]
            res.sort()
            self.assertListEqual(expected[i], res)

    def test_fourSum3(self):
        x = Solution()
        result = x.fourSum([2,2,2,2,2], 8)
        expected = [[2,2,2,2]]
        self.assertEqual(len(expected), len(result))
        for i in range(len(result)):
            res = result[i]
            res.sort()
            self.assertListEqual(expected[i], res)

    def test_fourSum4(self):
        x = Solution()
        result = x.fourSum([0], 0)
        self.assertEqual([], result)

    def test_fourSum5(self):
        x = Solution()
        result = x.fourSum([-3,-1,0,2,4,5], 0)
        expected = [[-3,-1,0,4]]
        self.assertEqual(len(expected), len(result))
        for i in range(len(result)):
            res = result[i]
            res.sort()
            self.assertListEqual(expected[i], res)

    def test_fourSum6(self):
        x = Solution()
        result = x.fourSum([-3,-1,0,2,4,5], 2)
        expected = [[-3,-1,2,4]]
        self.assertEqual(len(expected), len(result))
        for i in range(len(result)):
            res = result[i]
            res.sort()
            self.assertListEqual(expected[i], res)

    def test_fourSum7(self):
        x = Solution()
        result = x.fourSum([0,0,0,0], 0)
        expected = [[0,0,0,0]]
        self.assertEqual(len(expected), len(result))
        for i in range(len(result)):
            res = result[i]
            res.sort()
            self.assertListEqual(expected[i], res)

