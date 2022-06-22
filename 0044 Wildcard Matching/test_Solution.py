from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_regex_match1(self):
        x = Solution()
        self.assertFalse(x.isMatch("aa", "a"))

    def test_regex_match2(self):
        x = Solution()
        self.assertTrue(x.isMatch("aa", "*"))

    def test_regex_match3(self):
        x = Solution()
        self.assertFalse(x.isMatch("cb", "?a"))

    def test_regex_match4(self):
        x = Solution()
        self.assertTrue(x.isMatch("abccced", "a?*d"))

    def test_regex_match5(self):
        x = Solution()
        self.assertTrue(x.isMatch("abd", "a?*d"))

    def test_regex_match6(self):
        x = Solution()
        self.assertFalse(x.isMatch("abcccd", "a?*dd"))

    def test_regex_match7(self):
        x = Solution()
        self.assertFalse(x.isMatch("abcccd", "a*dd"))

    def test_regex_match8(self):
        x = Solution()
        self.assertTrue(x.isMatch("abcccde", "a*de"))

    def test_regex_match9(self):
        x = Solution()
        self.assertTrue(x.isMatch("abcccde", "a*e"))

    def test_regex_match10(self):
        x = Solution()
        self.assertTrue(x.isMatch("aaa", "*a"))

    def test_regex_match11(self):
        x = Solution()
        self.assertTrue(x.isMatch("mississippi", "mi*i**?"))

    def test_regex_match12(self):
        x = Solution()
        self.assertTrue(x.isMatch("aabcbcbcaccbcaabc", "*a*a*?**?***"))

    def test_regex_match13(self):
        x = Solution()
        self.assertTrue(x.isMatch("abcaaaaaaabaabcabac", "*ab?a******"))

    def test_regex_match14(self):
        x = Solution()
        self.assertTrue(x.isMatch("abcd", "*"))

    def test_regex_match15(self):
        x = Solution()
        self.assertFalse(x.isMatch("babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab","***bba**a*bbba**aab**b"))

    def test_regex_match16(self):
        x = Solution()
        self.assertFalse(x.isMatch("babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb","b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"))
