from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_decode_string1(self):
        x = Solution()
        self.assertEqual("aaabcbc", x.decodeString("3[a]2[bc]"))

    def test_decode_string2(self):
        x = Solution()
        self.assertEqual("accaccacc", x.decodeString("3[a2[c]]"))

    def test_decode_string3(self):
        x = Solution()
        self.assertEqual("abcabccdcdcdef", x.decodeString("2[abc]3[cd]ef"))

    def test_decode_string4(self):
        x = Solution()
        self.assertEqual("trabcabccdcdcdef", x.decodeString("tr2[abc]3[cd]ef"))

    def test_decode_string5(self):
        x = Solution()
        self.assertEqual("aaaaaaaaaaaa", x.decodeString("12[a]"))
