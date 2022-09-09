from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_method1(self):
        x = Solution()
        self.assertEqual(4, x.method([
            [1,0,0],
            [0,0,0],
            [0,0,1]]))

    def test_method2(self):
        x = Solution()
        self.assertEqual(6, x.method([
            [1,1,0],
            [0,0,0],
            [0,1,1]]))

    def test_method3(self):
        x = Solution()
        self.assertEqual(6, x.method([
            [1,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,1]]))

    def test_method4(self):
        x = Solution()
        self.assertEqual(12, x.method([
            [1,0,0,0,1],
            [0,0,0,0,0],
            [1,0,0,0,1]]))

    def test_method5(self):
        x = Solution()
        self.assertEqual(7, x.method([
            [1,0,0,0,0],
            [0,0,0,0,1],
            [0,0,0,0,1]]))
