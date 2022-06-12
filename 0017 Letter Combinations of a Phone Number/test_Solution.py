from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_letterCombinations1(self):
        x = Solution()
        self.assertEqual(["ad","ae","af","bd","be","bf","cd","ce","cf"], x.letterCombinations("23"))

    def test_letterCombinations2(self):
        x = Solution()
        self.assertEqual([], x.letterCombinations(""))

    def test_letterCombinations3(self):
        x = Solution()
        self.assertEqual(["a", "b", "c"], x.letterCombinations("2"))
