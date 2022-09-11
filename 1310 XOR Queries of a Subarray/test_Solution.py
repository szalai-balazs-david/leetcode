from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_xor_queries(self):
        x = Solution()
        self.assertListEqual([2,7,14,8], x.xorQueries([1,3,4,8], [[0,1],[1,2],[0,3],[3,3]]))
