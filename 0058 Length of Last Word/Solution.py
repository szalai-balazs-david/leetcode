class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")
        words.reverse()
        for word in words:
            if len(word) > 0:
                return len(word)
        return -1
