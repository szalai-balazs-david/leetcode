from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_findSubstring1(self):
        x = Solution()
        self.assertListEqual([0,9], x.findSubstring("barfoothefoobarman", ["foo","bar"]))

    def test_findSubstring2(self):
        x = Solution()
        self.assertListEqual([], x.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]))

    def test_findSubstring3(self):
        x = Solution()
        self.assertListEqual([6,9,12], x.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))
