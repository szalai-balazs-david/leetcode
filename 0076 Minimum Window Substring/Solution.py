from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        target = Counter(t)
        letters = {}
        for c in target:
            letters[c] = 0

        done = False

        def is_complete():
            nonlocal done
            if done:
                return True
            for c in target:
                if target[c] > letters[c]:
                    return False
            done = True
            return True

        left = 0
        result = ""
        for right in range(len(s)):
            if s[right] in letters:
                letters[s[right]] += 1
                if is_complete():
                    for l in range(left, right + 1):
                        if s[l] in letters:
                            if letters[s[l]] > target[s[l]]:
                                letters[s[l]] -= 1
                            else:
                                left = l
                                sub_result = s[left:right + 1]
                                if result == "" or len(sub_result) < len(result):
                                    result = sub_result
                                break
        return result
