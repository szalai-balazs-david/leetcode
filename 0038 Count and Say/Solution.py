class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        say = self.countAndSay(n - 1)

        result = ""
        i = 0
        while i < len(say):
            num = say[i]
            j = i
            while j < len(say) and say[j] == say[i]:
                j += 1
            result += str(j - i) + str(num)
            i = j

        return result
