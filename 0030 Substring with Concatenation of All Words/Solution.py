import re


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        result = []

        indices = {}
        for word in words:
            if word in indices.values():
                continue
            locations = [m.start() for m in re.finditer(f"(?={word})", s)]
            for location in locations:
                indices[location] = word
        word_length = len(words[0])

        for i in range(len(s) - len(words) * word_length + 1):

            if indices.get(i) is None:
                continue
            expected_indexes = []
            for j in range(len(words)):
                expected_indexes.append(i + j * word_length)
            remaining_words = words.copy()

            for expected_index in expected_indexes:
                if indices.get(expected_index) is not None:
                    if remaining_words.__contains__(indices[expected_index]):
                        remaining_words.remove(indices[expected_index])
                    else:
                        break
            if len(remaining_words) == 0:
                result.append(i)

        return result
    