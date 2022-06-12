from unittest import TestCase
from Solution import Solution


class TestSolution(TestCase):
    def test_longest_palindrome1(self):
        x = Solution()
        self.assertEqual("bab", x.longestPalindrome("babed"))

    def test_longest_palindrome2(self):
        x = Solution()
        self.assertEqual("bb", x.longestPalindrome("cbbd"))

    def test_longest_palindrome3(self):
        x = Solution()
        self.assertEqual("dbbd", x.longestPalindrome("dbbd"))

    def test_longest_palindrome4(self):
        x = Solution()
        self.assertEqual("a", x.longestPalindrome("ac"))

    def test_longest_palindrome5(self):
        x = Solution()
        self.assertEqual("khvhk", x.longestPalindrome("mwwfjysbkebpdjyabcfkgprtxpwvhglddhmvaprcvrnuxifcrjpdgnktvmggmguiiquibmtviwjsqwtchkqgxqwljouunurcdtoeygdqmijdympcamawnlzsxucbpqtuwkjfqnzvvvigifyvymfhtppqamlgjozvebygkxawcbwtouaankxsjrteeijpuzbsfsjwxejtfrancoekxgfyangvzjkdskhssdjvkvdskjtiybqgsmpxmghvvicmjxqtxdowkjhmlnfcpbtwvtmjhnzntxyfxyinmqzivxkwigkondghzmbioelmepgfttczskvqfejfiibxjcuyevvpawybcvvxtxycrfbcnpvkzryrqujqaqhoagdmofgdcbhvlwgwmsmhomknbanvntspvvhvccedzzngdywuccxrnzbtchisdwsrfdqpcwknwqvalczznilujdrlevncdsyuhnpmheukottewtkuzhookcsvctsqwwdvfjxifpfsqxpmpwospndozcdbfhselfdltmpujlnhfzjcgnbgprvopxklmlgrlbldzpnkhvhkybpgtzipzotrgzkdrqntnuaqyaplcybqyvidwcfcuxinchretgvfaepmgilbrtxgqoddzyjmmupkjqcypdpfhpkhitfegickfszermqhkwmffdizeoprmnlzbjcwfnqyvmhtdekmfhqwaftlyydirjnojbrieutjhymfpflsfemkqsoewbojwluqdckmzixwxufrdpqnwvwpbavosnvjqxqbosctttxvsbmqpnolfmapywtpfaotzmyjwnd"))

    def test_longest_palindrome6(self):
        x = Solution()
        self.assertEqual("abcdefedcba", x.longestPalindrome("abcdefedcbae"))
