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
        self.assertEqual(7, x.search([4,5,6,7,8,9,10,0,1,2], 0))

    def test_search4(self):
        x = Solution()
        self.assertEqual(3, x.search([4,5,6,7,8,9,10,0,1,2], 7))

    def test_search5(self):
        x = Solution()
        self.assertEqual(-1, x.search([1], 0))

    def test_search6(self):
        x = Solution()
        self.assertEqual(-1, x.search([1,3], 0))

    def test_search7(self):
        x = Solution()
        self.assertEqual(1, x.search([1,3], 3))

    def test_search8(self):
        x = Solution()
        self.assertEqual(0, x.search([3,1], 3))

    def test_search9(self):
        x = Solution()
        self.assertEqual(-1, x.search([3,5,1], 0))

    def test_search10(self):
        x = Solution()
        self.assertEqual(2, x.search([3,5,1], 1))
