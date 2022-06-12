class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0
        stage = 1 # 1: whitespace, 2: sign, 3: number
        is_negative = False

        for c in s:
            if stage == 2:
                stage = 3
            if stage == 1:
                if c == " ":
                    continue
                else:
                    stage = 2
            if stage == 2:
                if c == "-":
                    is_negative = True
                elif c != "+":
                    stage = 3
            if stage == 3:
                match c:
                    case "0":
                        result = result * 10
                    case "1":
                        result = result * 10 + 1
                    case "2":
                        result = result * 10 + 2
                    case "3":
                        result = result * 10 + 3
                    case "4":
                        result = result * 10 + 4
                    case "5":
                        result = result * 10 + 5
                    case "6":
                        result = result * 10 + 6
                    case "7":
                        result = result * 10 + 7
                    case "8":
                        result = result * 10 + 8
                    case "9":
                        result = result * 10 + 9
                    case _:
                        break

        result = -1 * result if is_negative else result
        if result < -(2**31):
            result = -(2**31)
        elif result > 2**31 - 1:
            result = 2**31 - 1
        return result
