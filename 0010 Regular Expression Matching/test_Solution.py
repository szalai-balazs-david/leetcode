from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_regex_match1(self):
        x = Solution()
        self.assertFalse(x.isMatch("aa", "a"))

    def test_regex_match2(self):
        x = Solution()
        self.assertTrue(x.isMatch("aa", "a*"))

    def test_regex_match3(self):
        x = Solution()
        self.assertTrue(x.isMatch("aa", ".*"))

    def test_regex_match4(self):
        x = Solution()
        self.assertTrue(x.isMatch("abcccd", "a.c*d"))

    def test_regex_match5(self):
        x = Solution()
        self.assertTrue(x.isMatch("abd", "a.c*d"))

    def test_regex_match6(self):
        x = Solution()
        self.assertFalse(x.isMatch("abcccd", "a.c*dd"))

    def test_regex_match7(self):
        x = Solution()
        self.assertFalse(x.isMatch("abcccd", "a.*dd"))

    def test_regex_match8(self):
        x = Solution()
        self.assertTrue(x.isMatch("abcccde", "a.*de"))

    def test_regex_match9(self):
        x = Solution()
        self.assertTrue(x.isMatch("abcccde", "a.*e"))

    def test_regex_match10(self):
        x = Solution()
        self.assertTrue(x.isMatch("aaa", "a*a"))

    def test_regex_match11(self):
        x = Solution()
        self.assertFalse(x.isMatch("mississippi", "mis*is*p*."))

    def test_regex_match12(self):
        x = Solution()
        self.assertTrue(x.isMatch("aabcbcbcaccbcaabc", ".*a*aa*.*b*.c*.*a*"))

    def test_regex_match13(self):
        x = Solution()
        self.assertTrue(x.isMatch("abcaaaaaaabaabcabac", ".*ab.a.*a*a*.*b*b*"))

    def test_regex_match14(self):
        x = Solution()
        self.assertFalse(x.isMatch("abcd", "d*"))

    def test_regex_match15(self):
        x = {}
        print(x)
        x[1, 3] = True
        print(x)
        print(x[1, 3])
        print(x[1])
        self.fail()
