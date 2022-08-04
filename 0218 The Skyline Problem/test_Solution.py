from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_get_skyline1(self):
        x = Solution()
        input = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
        expected = [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
        actual = x.getSkyline(input)
        self.assertListEqual(expected, actual)

    def test_get_skyline2(self):
        x = Solution()
        input = [[0,2,3],[2,5,3]]
        expected = [[0,3],[5,0]]
        actual = x.getSkyline(input)
        self.assertListEqual(expected, actual)

    def test_get_skyline3(self):
        x = Solution()
        input = [[1,2,1],[1,2,2],[1,2,3]]
        expected = [[1,3],[2,0]]
        actual = x.getSkyline(input)
        self.assertListEqual(expected, actual)
