from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_rotate1(self):
        x = Solution()
        expected = [[7,4,1],[8,5,2],[9,6,3]]
        actual = [[1,2,3],[4,5,6],[7,8,9]]
        x.rotate(actual)
        for i in range(len(actual)):
            self.assertListEqual(expected[i], actual[i])

    def test_rotate2(self):
        x = Solution()
        expected = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
        actual = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        x.rotate(actual)
        for i in range(len(actual)):
            self.assertListEqual(expected[i], actual[i])

    def test_rotate3(self):
        x = Solution()
        expected = [[21,16,11,6,1],[22,17,12,7,2],[23,18,13,8,3],[24,19,14,9,4],[25,20,15,10,5]]
        actual = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
        x.rotate(actual)
        for i in range(len(actual)):
            self.assertListEqual(expected[i], actual[i])
