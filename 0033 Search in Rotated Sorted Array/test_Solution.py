from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_search1(self):
        x = Solution()
        self.assertEqual(4, x.search([4,5,6,7,0,1,2], 0))

    def test_search2(self):
        x = Solution()
        self.assertEqual(-1, x.search([4,5,6,7,0,1,2], 3))

    def test_search3(self):
        x = Solution()
        self.assertEqual(-1, x.search([1], 0))
