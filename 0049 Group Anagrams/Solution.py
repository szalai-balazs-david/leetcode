class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dict = {}

        for word in strs:
            arr = list(word)
            arr.sort()
            new_word = str(arr)
            if new_word in dict:
                dict[new_word].append(word)
            else:
                dict[new_word] = [word]

        return list(dict.values())
