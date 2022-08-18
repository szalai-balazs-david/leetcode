from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_insert1(self):
        x = Solution()
        expected = [[1,5],[6,9]]
        actual = x.insert([[1,3],[6,9]], [2,5])
        self.assertListEqual(expected, actual)

    def test_insert2(self):
        x = Solution()
        expected = [[1,2],[3,10],[12,16]]
        actual = x.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])
        self.assertListEqual(expected, actual)

    def test_insert3(self):
        x = Solution()
        expected = [[1,3],[4,5],[6,9]]
        actual = x.insert([[1,3],[6,9]], [4,5])
        self.assertListEqual(expected, actual)

    def test_insert4(self):
        x = Solution()
        expected = [[1,3],[6,10]]
        actual = x.insert([[1,3],[6,9]], [9,10])
        self.assertListEqual(expected, actual)

    def test_insert5(self):
        x = Solution()
        expected = [[1,3],[6,9],[10,11]]
        actual = x.insert([[1,3],[6,9]], [10,11])
        self.assertListEqual(expected, actual)
