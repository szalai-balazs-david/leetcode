from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_longestValidParentheses1(self):
        x = Solution()
        self.assertEqual(2, x.longestValidParentheses("(()"))

    def test_longestValidParentheses2(self):
        x = Solution()
        self.assertEqual(4, x.longestValidParentheses(")()())"))

    def test_longestValidParentheses3(self):
        x = Solution()
        self.assertEqual(0, x.longestValidParentheses(""))
