from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_generateParenthesis1(self):
        x = Solution()
        expected = ["((()))","(()())","(())()","()(())","()()()"]
        actual = x.generateParenthesis(3)
        self.assertEqual(len(expected), len(actual))
        for i in range(len(actual)):
            self.assertTrue(expected.__contains__(actual[i]))
        for i in range(len(expected)):
            self.assertTrue(actual.__contains__(expected[i]))

    def test_generateParenthesis2(self):
        x = Solution()
        expected = ["()"]
        actual = x.generateParenthesis(1)
        self.assertEqual(len(expected), len(actual))
        for i in range(len(actual)):
            self.assertTrue(expected.__contains__(actual[i]))
        for i in range(len(expected)):
            self.assertTrue(actual.__contains__(expected[i]))
