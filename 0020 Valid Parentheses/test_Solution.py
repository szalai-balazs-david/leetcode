from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_isValid1(self):
        x = Solution()
        self.assertTrue(x.isValid("()"))

    def test_isValid2(self):
        x = Solution()
        self.assertTrue(x.isValid("()[]{}"))

    def test_isValid3(self):
        x = Solution()
        self.assertFalse(x.isValid("(]"))

    def test_isValid4(self):
        x = Solution()
        self.assertFalse(x.isValid("("))

    def test_isValid5(self):
        x = Solution()
        self.assertTrue(x.isValid("(()[]{})"))

    def test_isValid6(self):
        x = Solution()
        self.assertFalse(x.isValid("(()[]{)}"))
