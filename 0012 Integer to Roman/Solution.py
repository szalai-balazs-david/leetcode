class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""

        letters = [["I", "V", "X"], ["X", "L", "C"], ["C", "D", "M"], ["M", "", ""]]

        for l in letters:
            digit = num % 10
            num = int(num / 10)
            match digit:
                case x if 1 <= x < 4:
                    for i in range(x):
                        result += l[0]
                case 4:
                    result += l[1] + l[0]
                case 5:
                    result += l[1]
                case x if 6 <= x < 9:
                    for i in range(x - 5):
                        result += l[0]
                    result += l[1]
                case 9:
                    result += l[2] + l[0]
            if num == 0:
                break

        return result[::-1]