from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_word_break1(self):
        x = Solution()
        self.assertEqual(True, x.wordBreak("leetcode", ["leet", "code"]))

    def test_word_break2(self):
        x = Solution()
        self.assertEqual(True, x.wordBreak("applepenapple", ["apple","pen"]))

    def test_word_break3(self):
        x = Solution()
        self.assertEqual(False, x.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))
