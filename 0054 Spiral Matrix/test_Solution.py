from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_spiral_order1(self):
        x = Solution()
        self.assertListEqual([1,2,3,6,9,8,7,4,5], x.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))

    def test_spiral_order2(self):
        x = Solution()
        self.assertListEqual([1,2,3,4,8,12,11,10,9,5,6,7], x.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))

    def test_spiral_order3(self):
        x = Solution()
        self.assertListEqual([7,9,6], x.spiralOrder([[7],[9],[6]]))
