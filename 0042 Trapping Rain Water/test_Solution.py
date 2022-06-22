from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_trap1(self):
        x = Solution()
        self.assertEqual(6, x.trap([0,1,0,2,1,0,1,3,2,1,2,1]))

    def test_trap2(self):
        x = Solution()
        self.assertEqual(9, x.trap([4,2,0,3,2,5]))

    def test_trap3(self):
        x = Solution()
        self.assertEqual(1, x.trap([4,2,3]))
