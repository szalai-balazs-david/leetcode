class Solution:
    def longestPalindrome(self, s: str) -> str:
        print(s)
        if s == s[::-1]: return s

        start, size = 0, 1
        for i in range(1, len(s)):
            l, r = i - size, i + 1
            s1, s2 = s[l-1:r], s[l:r]
            print(f"start = {start}, size={size}, i={i}, l={l}, r={r}, s1={s1}, s2={s2}")

            if l - 1 >= 0 and s1 == s1[::-1]:
                start, size = l - 1, size + 2
                print(f"In IF start = {start}, size={size}")
            elif s2 == s2[::-1]:
                start, size = l, size + 1
                print(f"In ELIF start = {start}, size={size}")

        return s[start:start+size]
