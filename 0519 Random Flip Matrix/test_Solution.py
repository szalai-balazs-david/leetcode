from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test1(self):
        x = Solution(2,2)
        print(x.flip())
        print(x.flip())
        print(x.flip())
        print(x.flip())
        x.reset()
