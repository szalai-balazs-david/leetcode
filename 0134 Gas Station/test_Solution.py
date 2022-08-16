from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_can_complete_circuit1(self):
        x = Solution()
        self.assertEqual(3, x.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))

    def test_can_complete_circuit2(self):
        x = Solution()
        self.assertEqual(-1, x.canCompleteCircuit([2,3,4], [3,4,3]))

    def test_can_complete_circuit3(self):
        x = Solution()
        self.assertEqual(0, x.canCompleteCircuit([4,5,1,2,3], [1,2,3,4,5]))

    def test_can_complete_circuit4(self):
        x = Solution()
        self.assertEqual(1, x.canCompleteCircuit([1,2], [2,1]))
