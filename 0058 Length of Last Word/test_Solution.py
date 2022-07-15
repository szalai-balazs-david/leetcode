from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_length_of_last_word1(self):
        x = Solution()
        self.assertEqual(5, x.lengthOfLastWord("Hello World"))

    def test_length_of_last_word2(self):
        x = Solution()
        self.assertEqual(4, x.lengthOfLastWord("   fly me   to   the moon  "))

    def test_length_of_last_word3(self):
        x = Solution()
        self.assertEqual(6, x.lengthOfLastWord("luffy is still joyboy"))
